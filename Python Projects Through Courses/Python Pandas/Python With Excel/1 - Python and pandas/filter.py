import pandas as pd

df = pd.read_csv("data.csv")
df.columns = ["Duration", "Pulse", "Maxpulse", "Calories"]

# will search 117 - like WHERE in SQL
# print(df.loc[df["Pulse"] == 117])

# will search 117 and 45
# print(df.loc[(df["Pulse"] == 117) & (df["Duration"] == 45)])

# df["Maximum_Pulse"] = df["Maxpulse"].apply(
# lambda x: 100 if 100 < x < 200 else 200 if 200 < x < 300 else 0
# )

# df["Maximum Calories"] = df["Maxpulse"] * df["Calories"]

# to_drop = ["Duration", "Maxpulse", "Calories"]
# df.drop(columns=to_drop, inplace=True)

df["Test Col"] = False
df.loc[df["Maxpulse"] < 100, "Test Col"] = True

print(df.groupby(["Test Col"]).mean().sort_values("Maxpulse"))
