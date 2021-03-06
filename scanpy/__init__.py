# Author: F. Alex Wolf (http://falexwolf.de)
#         P. Angerer
"""Scanpy - Single-Cell Analysis in Python

Reference
---------
Wolf, Angerer & Theis, bioRxiv doi:... (2017)
"""

import sys
import warnings
if (sys.version_info < (3, 0)):
    warnings.warn('Scanpy only runs reliably with Python 3, preferrably >=3.5.')

# version generated by versioneer
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
