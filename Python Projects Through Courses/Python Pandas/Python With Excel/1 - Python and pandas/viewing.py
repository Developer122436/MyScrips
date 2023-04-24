import pandas as pd
from openpyxl.workbook import workbook

df_csv = pd.read_csv("data.csv")
df_csv.columns = ["Duration", "Pulse", "Maxpulse", "Calories"]

# Checks last column values
# print(df_csv["Calories"])

# Checks 2 lasts column values
# print(df_csv[["Maxpulse", "Calories"]])

# Shows only 3 first rows of duration
# print(df_csv["Duration"][0:3])

# It will save only the mentioned columns
wanted_values = df_csv[["Duration", "Pulse", "Maxpulse"]]
stored = wanted_values.to_excel("Duration_calories.xlsx")
