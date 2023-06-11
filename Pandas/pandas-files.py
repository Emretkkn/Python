import sqlite3
import pandas as pd
# df = pd.read_csv("nba\player_data.csv")
# df = pd.read_json("person.json",encoding="UTF-8")
df = pd.read_excel("nba/Players.xlsx")
# connection = sqlite3.connect("kdsproje.sql")
# df = pd.read_sql_query("SELECT * FROM model",connection)
print(df)