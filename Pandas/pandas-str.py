import pandas as pd
import numpy as np
data = pd.read_csv("nba/player_data.csv")
data.dropna(inplace=True)
# data["name"] = data["name"].str.upper()
# data["name"] = data["name"].str.lower()
# data["index"] = data["name"].str.find("a")
# data = data[data["name"].str.contains("Abdul")]
# data = data.college.str.replace(" ","-")
# print(data.head(10)
# data[["First Name","Last Name"]] = data["name"].loc[data["name"].str.split().str.len()==2].str.split(expand=True)
# data[["First Name","Last Name"]] = data["name"].loc[data["name"].str.split().str.len()==2].str.split(expand=True)
print(data.head(10))
