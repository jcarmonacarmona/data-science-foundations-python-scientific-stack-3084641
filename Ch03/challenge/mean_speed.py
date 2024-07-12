# What is the mean speed (mile/hour) in taxi.parquet?

# - Run download_data.py to download the data
# %%
import pandas as pd

parquet_file = '/workspaces/data-science-foundations-python-scientific-stack-3084641/taxi.parquet'
df = pd.read_parquet(parquet_file)
#df = pd.read_csv(csv_file, parse_dates=['time'])
df

# %%
df[['tpep_pickup_datetime','tpep_dropoff_datetime','trip_distance']]

# %%
mask = df['tpep_dropoff_datetime'] > df['tpep_pickup_datetime']
df = df[mask]

# %%
times = df['tpep_dropoff_datetime']-df['tpep_pickup_datetime']
times_hour = times / pd.Timedelta(1, 'hour')
speed = df['trip_distance'] / times_hour
df['speed']

# %%
speed.mean()

# %%
