from entsoe import EntsoePandasClient, EntsoeRawClient
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil.relativedelta import *

localtime = datetime.today() + relativedelta(days=-30)
startTime = '{:04d}'.format(localtime.year) + '{:02d}'.format(localtime.month) + '{:02d}'.format(localtime.day)
localtime = datetime.today()
endTime = '{:04d}'.format(localtime.year) + '{:02d}'.format(localtime.month) + '{:02d}'.format(localtime.day)

start = pd.Timestamp(startTime, tz='Europe/Vienna')
end = pd.Timestamp(endTime, tz='Europe/Vienna')
country_code = 'AT'

client = EntsoePandasClient(api_key='---')
data=client.query_load(country_code=country_code, start=start, end=end)
#data.plot()
#plt.show()

clientRaw = EntsoeRawClient(api_key='---')
data2=clientRaw.query_imbalance_prices(country_code=country_code, start=start, end=end)
