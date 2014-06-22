from pyHRV.galaxy.ParamExecClass import ParamExecClass
from pyHRV.Files import load_rr, save_data_series
from pyHRV.Filters import RRFilters

__author__ = 'AleB'


class GalaxyFilter(ParamExecClass):
    """
    T_RR_CSV -> T_RR_CSV
    kwargs['input'] ----> input file
    kwargs['output'] ---> output file
    """

    def execute(self):
        inp = self._kwargs['input']
        out = self._kwargs['output']
        save_data_series(RRFilters.filter_outliers(load_rr(inp)), out)
