import pandas as pd

df = pd.read_csv("data.csv")
# use to_string() to print the entire DataFrame.
# print(df.to_string())
# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows
# print(df)

# Check the number of maximum returned rows
print(pd.options.display.max_rows)

# Increase the maximum number of rows to display the entire DataFrame:
pd.options.display.max_rows = 9999
