from quickBayes.functions.qldata_function import QlDataFunction
from quickBayes.utils.spline import spline
from quickBayes.utils.general import get_background_function
from quickBayes.workflow.model_template import ModelSelectionWorkflow
from quickBayes.functions.base import BaseFitFunction
from quickBayes.utils.crop_data import crop


from numpy import ndarray
import numpy as np
from typing import Dict, List


class QLData(ModelSelectionWorkflow):
    """
    A class for the quasielastic lorentzian workflow
    """
    def preprocess_data(self, x_data: ndarray,
                        y_data: ndarray, e_data: ndarray,
                        start_x: float, end_x: float,
                        res: Dict[str, ndarray]) -> (ndarray, ndarray):
        """
        The preprocessing needed for the data.
        It splines the sample and resolution data
        to the same uniform grid.
        :param x_data: the sample x data to fit to
        :param y_data: the sample y data to fit to
        :param e_data: the sample errors for the y data
        :param start_x: the start x value
        :param end_x: the end x value
        :param res: a dict of the resolution data (keys =x, y, e)
        :return the new x range and the new resolution y values
        """
        dx = x_data[1] - x_data[0]
        new_x = np.linspace(start_x, end_x, int((end_x - start_x)/dx))

        sy = spline(x_data, y_data, new_x)
        se = spline(x_data, e_data, new_x)
        ry = spline(res['x'], res['y'], new_x)
        super().preprocess_data(new_x, sy, se)

        # Set the raw data
        raw_x, raw_y, raw_e = crop(x_data, y_data, e_data,
                                   start_x, end_x)
        self._raw = {'x': raw_x, 'y': raw_y, 'e': raw_e}

        return new_x, ry

    @staticmethod
    def _update_function(func: BaseFitFunction) -> BaseFitFunction:
        """
        This method adds a single lorentzian to the fitting function
        :param func: the fitting function that needs modifying
        :return the modified fitting function
        """
        func.add_single_lorentzian()
        return func


def ql_data_main(sample: Dict[str, ndarray], res: Dict[str, ndarray],
                 BG_type: str, start_x: float, end_x: float,
                 elastic: bool,
                 results: Dict[str, ndarray],
                 results_errors: Dict[str, ndarray],
                 init_params: List[float] = None) -> (Dict[str, ndarray],
                                                      Dict[str, ndarray],
                                                      ndarray,
                                                      List[ndarray],
                                                      List[ndarray]):
    """
    Method for wrapping the qldata workflow.
    :param sample: dict containing the sample x, y and e data (keys = x, y, e)
    :param res: dict containing the resolution x, y data (keys = x, y)
    :param BG_type: the type of BG ("none", "flat", "linear")
    :param start_x: the start x for the calculation
    :param end_x: the end x for the calculation
    :param elastic: if to include the elastic peak
    :param results: dict of results
    :param results_errors: dict of errors for results
    :param init_params: initial values, if None a guess will be made
    :result dict of the fit parameters, their errors, the x range used, list of
    fit values and their errors.
    """

    # setup workflow
    workflow = QLData(results, results_errors)
    new_x, ry = workflow.preprocess_data(sample['x'], sample['y'],
                                         sample['e'],
                                         start_x, end_x, res)

    max_num_peaks = 3

    # setup fit function
    BG = get_background_function(BG_type)
    func = QlDataFunction(BG, elastic, new_x, ry, start_x, end_x)
    lower, upper = func.get_bounds()

    params = init_params if init_params is not None else func.get_guess()
    # just want a guess the same length as lower, it is not used
    workflow.set_scipy_engine(func.get_guess(), lower, upper)

    # do the calculation
    func = workflow.execute(max_num_peaks, func, params)
    results, results_errors = workflow.get_parameters_and_errors

    engine = workflow.fit_engine
    fits = []
    errors_fit = []
    x_data = []
    for j in range(max_num_peaks):
        x_data, y, e, df, de = engine.get_fit_values(j)
        fits.append(y)
        errors_fit.append(e)
    return results, results_errors, x_data, fits, errors_fit
