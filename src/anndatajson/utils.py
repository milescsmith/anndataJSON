from functools import wraps

import numpy as np
import scipy as sp


def add_method(cls):
    """from https://stackoverflow.com/a/59089116
    can't say I completely understand this at the moment, but this allows us to bind
    a new function to an existing class definition
    so, for instance, I can add a `filter_by` function to pandas.DataFrame
    without creating a new class that inherits from DataFrame
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        setattr(cls, func.__name__, wrapper)
        return func

    return decorator


# Using this class makes it much easier to save the array portions of
# an Anndata object, especially the arrays that may be in sparse format
# class NumpyEncoder(JSONEncoder):
#     """ Special json encoder for numpy types """
#     def default(self, obj):
#         if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
#             np.int16, np.int32, np.int64, np.uint8,
#             np.uint16,np.uint32, np.uint64)):
#             return int(obj)
#         elif isinstance(obj, (np.float_, np.float16, np.float32,
#             np.float64)):
#             return float(obj)
#         elif isinstance(obj,(np.ndarray,)): #### This is the fix
#             return obj.tolist()
#         elif isinstance(obj, (sp.sparse.csr_matrix, sp.sparse.csc_matrix)):
#             return obj.todense().tolist()
#         return JSONEncoder.default(self, obj)


def default(obj):
    if isinstance(
        obj,
        (
            np.int_,
            np.intc,
            np.intp,
            np.int8,
            np.int16,
            np.int32,
            np.int64,
            np.uint8,
            np.uint16,
            np.uint32,
            np.uint64,
        ),
    ):
        return int(obj)
    elif isinstance(obj, (np.float_, np.float16, np.float32, np.float64)):
        return float(obj)
    elif isinstance(obj, (np.ndarray,)):
        return obj.tolist()
    elif isinstance(obj, (sp.sparse.csr_matrix, sp.sparse.csc_matrix)):
        return obj.todense().tolist()
    else:
        return obj
