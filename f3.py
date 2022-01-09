#Import the required packages.
#Make sure that you have installed them before using it

import pandas as pd
from pandas_datareader import data as pdr
import mplfinance as fplt


print(dir(pdr))

#Assign variables ticker, sdate, size which is the brick size

ticker = "AMD"
sdate = "2020-01-01"
size = 2.5

#Use the get_data_yahoo() function to get the ticker and start date from variables
#get_data_yahoo() will get data from the assigned start date to recent date
#Save the data to dataframe

df = pdr.get_data_yahoo(ticker, start = sdate)

#Print the dataframe just for reference. You will see 6 columns and the no. of rows
#will change depending on the start date value

print(df)

#call the fplt.plot function and execute

fplt.plot(df,type='renko',renko_params=dict(brick_size=size),style='yahoo',figsize =(18,7), title = "RENKO CHART FOR {0}".format(ticker))