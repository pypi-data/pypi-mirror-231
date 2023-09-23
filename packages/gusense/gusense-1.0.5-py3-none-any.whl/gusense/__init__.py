

from .common.credit import auth
from api import data_api as da


def __getattr__(method_name):
    ta = da.goco_api()
    return getattr(ta, method_name)






