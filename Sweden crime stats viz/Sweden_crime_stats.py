import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("reported.csv", sep=";")
print(df.head())

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(x=df["Year"], y=df["crimes_total"], name="Crimes Committed"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df["Year"], y=df["population"], name="Population"),
    secondary_y=True,
)

fig.update_layout(
    title_text="Swedish Total Crimes Committed vs Population"
)

fig.update_xaxes(title_text="Year")

fig.update_yaxes(title_text="<b>primary</b> Crimes Committed", secondary_y=False)
fig.update_yaxes(title_text="<b>secondary</b> Population", secondary_y=True)

fig.show()


