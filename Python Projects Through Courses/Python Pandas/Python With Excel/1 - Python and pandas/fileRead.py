import pandas as pd
from openpyxl.workbook import Workbook

df_excel = pd.read_excel(r"Data\xlsx\regions.xlsx")
df_csv = pd.read_csv(r"Data\data.csv")
# df_txt = pd.read_csv(r"Data\data.txt", delimeter="\t")

print(df_csv)

# df_csv.columns = ["Duration", "Pulse", "Maxpulse", "Calories"]

# df_csv.to_excel("modified.xlsx")

# print(df_csv)
