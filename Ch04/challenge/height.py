# Draw the running track from track.csv
#
# - Sample data to a minute interval
# - Markers should be blue if the height is below 100 meter, otherwise red


# %%
import pandas as pd

df = pd.read_csv(
    '/workspaces/data-science-foundations-python-scientific-stack-3084641/Ch04/challenge/track.csv',
    parse_dates=['time'],
    index_col='time',
)
df = df.resample('min').mean()
df.head()

# %%
import folium

center = [df['lat'].mean(), df['lng'].mean()]

m = folium.Map(
    location=center,
    zoom_start=15,
)

def add_marker(row):
    loc = tuple(row[['lat', 'lng']])
    marker = folium.CircleMarker(
        loc,
        radius=5,
        color='red' if row['height'] < 100 else 'blue',
        popup=row.name.strftime('%H:%M'),
    )
    marker.add_to(m)

df.apply(add_marker, axis=1)
m

# %%