# prices.py

from pandas.io.data import get_data_google
from pandas import rolling_std
from datetime import datetime, timedelta

start_date = '2012-01-01'
end_date = datetime.now() - timedelta(days=1)

athx = get_data_google('ATHX', start_date, end_date)
clbs = get_data_google('CLBS', start_date, end_date)

athx['3d'] = rolling_std(athx['Volume'], window=3)
clbs['3d'] = rolling_std(clbs['Volume'], window=3)
