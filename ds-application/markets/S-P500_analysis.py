#
# Code to combine earthquake data with S&P 500 prices 7 and 14 days and 1 month after incident
# Fix DATA_DIR to local to run
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

pd.options.mode.chained_assignment = None  # default='warn'

DATA_DIR = "/Users/wel51x/GDrive/Lambda/LambdaLabs/quake-viewer/ds-data/"

# fcn to get next trading day - needed when incident(s) occur on non-trading day
def get_next_trading_day(date_in):
  t1 = date_in
  dayz = 1
  while t1 not in df_sp500.index:
    t1 = pd.to_datetime(date_in).date() + datetime.timedelta(days=dayz)
    t1 = t1.strftime('%Y-%m-%d')
    dayz += 1
  return t1 

# prep S&P 500 df
sp500 = pd.read_csv("https://raw.githubusercontent.com/labs13-quake-viewer/ds-data/master/S%26P%20500.csv")

# code to reformat date - required 'cause python moronically formats 11/22/63 as 2063-11-22
dates=[]
for i in sp500['Date']:
  dd = datetime.datetime.strptime(i,'%m/%d/%y')
  if dd.year > 2019:
    dd = dd.replace(year=dd.year-100)
  dates.append(dd.strftime( '%Y-%m-%d' ))
sp500['Date'] = dates

#sp500.plot(x="Date", y="Close", figsize=(20, 10));

df_sp500 = sp500.set_index('Date')

# prep Quakes df
quakes = pd.read_csv("https://raw.githubusercontent.com/labs13-quake-viewer/ds-data/master/Earthquakes%205.5%201900-present.csv")

df_quakes = quakes[['time', 'mag', 'latitude', 'longitude']]
df_quakes.time = df_quakes.time.str[:10]
df_quakes = df_quakes.sort_values(by=['time'])

df = df_quakes[df_quakes['time'] >= "1950-01-03"]
df_quakes = df[df['mag'] >= 6.7]
df_quakes = df_quakes.reset_index(drop=True)

#df_quakes.plot(x="time", y="mag", figsize=(20, 10));

# create rows with date, mag, close, close+7, close+14, close+30
data = []
for _, row in df_quakes.iterrows():

  if row.time > "2019-04-15":
    continue
    
  t0 = get_next_trading_day(row.time)
  
  t1 = pd.to_datetime(row.time).date() + datetime.timedelta(days=7)
  t1 = t1.strftime('%Y-%m-%d')
  t1 = get_next_trading_day(t1)

  t2 = pd.to_datetime(row.time).date() + datetime.timedelta(days=14)
  t2 = t2.strftime('%Y-%m-%d')
  t2 = get_next_trading_day(t2)
  
  t3 = pd.to_datetime(row.time).date() + datetime.timedelta(days=30)
  t3 = t3.strftime('%Y-%m-%d')
  t3 = get_next_trading_day(t3)

  x = (row.time, row.mag, df_sp500.loc[t0].Close, df_sp500.loc[t1].Close,
       df_sp500.loc[t2].Close, df_sp500.loc[t3].Close)
  
  data.append(x)

# now jam into df
df_quake_sp500 = pd.DataFrame(data=data, columns=['Date', 'Mag', 'Price_Day_0', 'Price_Day_7', 'Price_Day_14', 'Price_Day_30'])

# create cells with pct diff for +7, +14, +30
df_quake_sp500["Appr_Day_7"] = 100 * (df_quake_sp500["Price_Day_7"] - df_quake_sp500["Price_Day_0"]) / df_quake_sp500["Price_Day_0"]
df_quake_sp500["Appr_Day_14"] = 100 * (df_quake_sp500["Price_Day_14"] - df_quake_sp500["Price_Day_0"]) / df_quake_sp500["Price_Day_0"]
df_quake_sp500["Appr_Day_30"] = 100 * (df_quake_sp500["Price_Day_30"] - df_quake_sp500["Price_Day_0"]) / df_quake_sp500["Price_Day_0"]

# print the counts
#print(df_quake_sp500.Mag.value_counts().sort_index())
data = pd.Series(df_quake_sp500.Mag.value_counts().sort_index())
df_quake_sp500_counts = pd.DataFrame(columns=['Mag', 'Ct'], index=[0])
df_quake_sp500_counts = pd.concat([df_quake_sp500_counts, data.to_frame()], ignore_index=True, sort=True)
df_quake_sp500_counts = df_quake_sp500_counts.iloc[1:]
df_quake_sp500_counts.Ct = data.index
df_quake_sp500_counts.columns = ['Mag', 'Count']
#print(df_quake_sp500_counts.T)

# get US quakes only & process
df_quakes_usa = df_quakes.query('32.5 <= latitude < 48.75').query('-123 <= longitude < -69')

data = []
for _, row in df_quakes_usa.iterrows():
  
  if row.time > "2019-04-15":
    continue
    
  t0 = get_next_trading_day(row.time)
  
  t1 = pd.to_datetime(row.time).date() + datetime.timedelta(days=7)
  t1 = t1.strftime('%Y-%m-%d')
  t1 = get_next_trading_day(t1)

  t2 = pd.to_datetime(row.time).date() + datetime.timedelta(days=14)
  t2 = t2.strftime('%Y-%m-%d')
  t2 = get_next_trading_day(t2)
  
  t3 = pd.to_datetime(row.time).date() + datetime.timedelta(days=30)
  t3 = t3.strftime('%Y-%m-%d')
  t3 = get_next_trading_day(t3)

  x = (row.time, row.mag, df_sp500.loc[t0].Close, df_sp500.loc[t1].Close,
            df_sp500.loc[t2].Close, df_sp500.loc[t3].Close)
  
  data.append(x)
df_quake_sp500_usa = pd.DataFrame(data=data, columns=['Date', 'Mag', 'Price_Day_0', 'Price_Day_7', 'Price_Day_14', 'Price_Day_30'])
df_quake_sp500_usa["Appr_Day_7"] = 100 * (df_quake_sp500_usa["Price_Day_7"] - df_quake_sp500_usa["Price_Day_0"]) / df_quake_sp500_usa["Price_Day_0"]
df_quake_sp500_usa["Appr_Day_14"] = 100 * (df_quake_sp500_usa["Price_Day_14"] - df_quake_sp500_usa["Price_Day_0"]) / df_quake_sp500_usa["Price_Day_0"]
df_quake_sp500_usa["Appr_Day_30"] = 100 * (df_quake_sp500_usa["Price_Day_30"] - df_quake_sp500_usa["Price_Day_0"]) / df_quake_sp500_usa["Price_Day_0"]

df_quake_sp500.to_csv(DATA_DIR + "S&P 500 Price Change by Earthquake.csv")
df_quake_sp500_usa.to_csv(DATA_DIR + "S&P 500 Price Change by Earthquake (USA).csv")
df_quake_sp500_counts.to_csv(DATA_DIR + "sp500_counts.csv")
