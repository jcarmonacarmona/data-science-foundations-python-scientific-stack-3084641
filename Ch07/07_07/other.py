# %%
import pandas as pd

df = pd.read_csv(
    '/workspaces/data-science-foundations-python-scientific-stack-3084641/Ch07/07_07/track.csv',
    parse_dates=['time'],
    index_col='time'
)
df = (
    df
    .resample('3min')
    .mean()
    .reset_index()
)
df.head()

# %%
import plotly.express as px

fig = px.bar(
    df,
    x='time',
    y='height',
)
fig

# %%
fig.write_html('track.html')
# %%
