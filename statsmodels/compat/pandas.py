from __future__ import absolute_import

from distutils.version import LooseVersion

import pandas


version = LooseVersion(pandas.__version__)


try:
    from pandas.api.types import is_numeric_dtype  # noqa:F401
except ImportError:
    from pandas.core.common import is_numeric_dtype  # noqa:F401

if version >= '0.20':
    try:
        from pandas.tseries import offsets as frequencies
    except ImportError:
        from pandas.tseries import frequencies
    data_klasses = (pandas.Series, pandas.DataFrame)
else:
    try:
        import pandas.tseries.frequencies as frequencies
    except ImportError:
        from pandas.core import datetools as frequencies  # noqa

    data_klasses = (pandas.Series, pandas.DataFrame,
                    pandas.WidePanel)

try:
    import pandas.testing as testing
except ImportError:
    import pandas.util.testing as testing

assert_frame_equal = testing.assert_frame_equal
assert_index_equal = testing.assert_index_equal
assert_series_equal = testing.assert_series_equal
RangeIndex = tuple()

try:
    from pandas.core.common import is_numeric_dtype
except ImportError:
    # Pandas <= 0.14
    def is_numeric_dtype(arr_or_dtype):
        # Crude implementation only suitable for array-like types
        try:
            tipo = arr_or_dtype.dtype.type
        except AttributeError:
            tipo = type(None)
        return (issubclass(tipo, (np.number, np.bool_)) and
                not issubclass(tipo, (np.datetime64, np.timedelta64)))
