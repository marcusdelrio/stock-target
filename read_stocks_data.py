#read in stocks data via googlefinance package

%pylab
import pandas_datareader.data as web
import datetime
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2013, 1, 27)
amd = web.DataReader("AMD", 'google', start, end)
amd.Close.plot()
