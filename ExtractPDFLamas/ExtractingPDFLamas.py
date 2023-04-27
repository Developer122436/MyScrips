import camelot as cm
import pandas as pd
import datetime as dt
import os
import sys

pd.options.mode.chained_assignment = None

pd.set_option('display.max_columns', None)

if not os.path.exists(sys.argv[1]):
    print("Invalid path!")
else:
    tables = cm.read_pdf(
        sys.argv[1],
        flavor='lattice', pages='all')

now = dt.datetime.now()

year = now.year - 1

df_to_csv = pd.DataFrame(columns=[f"תקרה {year}", f"שיעור {year}", "שם יישוב", "סמל היישוב"])

first_row = {f"תקרה {year}": f"תקרה {year}", f"שיעור {year}": f"שיעור {year}", 'שם יישוב': 'שם יישוב', 'סמל היישוב': 'סמל היישוב'}

df_to_csv.loc[-1] = first_row
df_to_csv.index = df_to_csv.index + 1
df_to_csv = df_to_csv.sort_index()

for table in tables:
    df = table.df
    df.columns = [f"תקרה {year}", f"שיעור {year}", "שם יישוב", "סמל היישוב"]

    df["שם יישוב"] = df["שם יישוב"].str[::-1]

    df["שם יישוב"] = df["שם יישוב"].str.replace('\n', '')

    df_to_csv = pd.concat([df_to_csv, df.iloc[1:, :]])

df_to_csv['שם יישוב'] = df_to_csv['שם יישוב'].replace({'-טלאל': 'טל-אל', 'נהרייה': 'נהריה'})

if not os.path.exists(sys.argv[2]):
    print("Invalid path!")
else:
    df_to_csv.to_csv(
        sys.argv[2],
        header=False, index=False, encoding='utf-8-sig')
