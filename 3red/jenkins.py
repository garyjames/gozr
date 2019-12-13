# coding: utf-8
from main import Secdef
secdef = Secdef()
secdef.load_instruments()
futures = secdef.get_count_by_type()
futures_grouped_by_underlying = secdef.get_count_by_underlying()
symbols = secdef.get_symbol()
futures
futures_grouped_by_underlying
secdef.pprint(futures_grouped_by_underlying)
all_grouped_by_underlying = secdef.get_count_by_underlying(security_type='all')
secdef.pprint(all_grouped_by_underlying)
