import random
import csv
import pandas as pd
import plotly.express as px
import plotly.figure_factory as pf
df = pd.read_csv("data.csv")
print()
fig = pf.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"])
fig.show()