
from common.credit import auth
from gusense.api import data_api as da

auth('ssd6e646e447af4bb8879e47bc9500c82c', '8e819524fdd7bd3c405d3857961d5978ded36530')
ta = da.to_api()
#data = ta.stock_list(ucs_code='', name="", page=1, page_size=20)
data = ta.trade_days()
print(data)