import pandas as pd
import matplotlib.pyplot as plt

# load S&P 500 df
df_quake_sp500 = pd.read_csv("https://raw.githubusercontent.com/labs13-quake-viewer/ds-data/master/" +
                             "S%26P%20500%20Price%20Change%20by%20Earthquake.csv")
df_quake_sp500_usa = pd.read_csv("https://raw.githubusercontent.com/labs13-quake-viewer/ds-data/master/" +
                                 "S%26P%20500%20Price%20Change%20by%20Earthquake%20(USA).csv")

# now plot the mean of the 30day grouped by earthquake magnitude
df = df_quake_sp500.groupby(['Mag'])['Appr_Day_30'].mean()
df.plot.bar(figsize=(16, 8));
plt.show()

# do same for quakes in US only
df = df_quake_sp500_usa.groupby(['Mag'])['Appr_Day_30'].mean()
df.plot.bar(figsize=(16, 8))
plt.show()
