# %%
import pandas as pd

csv_file = '/workspaces/data-science-foundations-python-scientific-stack-3084641/Ch05/05_01/taxi.csv'
df = pd.read_csv(csv_file)
print(f'{len(df):,}')

# %%
df.iloc[0]

# %%
df.dtypes

# %%
time_cols = [
    'tpep_pickup_datetime',
    'tpep_dropoff_datetime',
]
df = pd.read_csv(
    csv_file,
    parse_dates=time_cols,
)
df.dtypes
# %%
