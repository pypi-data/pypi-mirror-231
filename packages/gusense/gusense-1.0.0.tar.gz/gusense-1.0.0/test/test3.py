
import gusense as gs

gs.auth('ssa0a5a788d921422aae306840b6c7134f', '3550b1ec1ce0091536c52cec8970f7d99516315f')
a = gs.stock_list()
#a = gs.stock_company(ucs_code='', name="银行", a='aa', bcd='')
#a = gs.trade_days(page=1, page_size=20)
#a = gs.company_info(page=1, page_size=20)
#a = gs.company_manager(page=1, page_size=20)
#a = gs.shareholder_info(page=1, page_size=20)
#a = gs.daily_price(ucs_code='000001.SZ')
#a = gs.week_price(start_date='2023-07-29', end_date='2023-09-01')
#a = gs.month_price(start_date='2023-08-26', end_date='2023-09-01')
print(a)
