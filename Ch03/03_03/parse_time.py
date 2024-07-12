# %%
import pandas as pd

csv_file = '/workspaces/data-science-foundations-python-scientific-stack-3084641/Ch03/03_03/track.csv'
df = pd.read_csv(csv_file)
df.dtypes
# %%
df = pd.read_csv(csv_file, parse_dates=['time'])
df.dtypes

# %%
