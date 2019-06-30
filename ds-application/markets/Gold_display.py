import pandas as pd
import matplotlib.pyplot as plt

# load df
df_quake_gold = pd.read_csv("https://raw.githubusercontent.com/labs13-quake-viewer/ds-data/master/" +
                            "Gold%20Price%20Change%20by%20Earthquake.csv")

# now plot the mean of these grouped by earthquake magnitude
for i in ['Appr_Day_7', 'Appr_Day_14', 'Appr_Day_30']:
  df = df_quake_gold.groupby(['Mag'])[i].mean()
  df.plot.bar(figsize=(16, 8))
  plt.show()
