import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook

df = pd.read_csv(r"Data\data.csv")
# df.columns = ["Duration", "Pulse", "Maxpulse", "Calories"]

df.drop(columns="Maxpulse", inplace=True)

# df = df.set_index("Area Code")

# First Column Split
# df.Duration = df.Duration.str.split(expand=True)

# Replace all NaN to 'N/A'
df = df.replace(np.nan, "N/A", regex=True)

to_excel = df.to_excel("modified.xlsx")
