"""
Main Package: pyHRV
Contains:
DataSeries: Data structure with cache support (for intermediate values in the indices computation).
Filters: Scripts for cleaning and normalizing data.
Files: Scripts for loading data from and saving to files in various formats (CSV and EXCEL BVP, ECG, IBI..)
+ 2 sub-packages (indexes, windowing)
"""

__author__ = "AleB"
import Files
import Filters
import PyHRVSettings
import indexes
import windowing
import DataSeries as _Ds

__all__ = ['Files', 'PyHRVSettings', 'windowing', 'indexes', 'Filters']
__all__.extend(_Ds.__all__)
__all__.extend(Filters.__all__)
__all__.extend(Files.__all__)
__all__.extend(indexes.__all__)
__all__.extend(windowing.__all__)

from DataSeries import *
from Files import *
from PyHRVSettings import *
from indexes import *
from windowing import *
from Filters import *

del _Ds
