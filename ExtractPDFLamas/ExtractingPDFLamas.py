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

dfToCSV = pd.DataFrame(columns=[f"תקרה {year}", f"שיעור {year}", "שם יישוב", "סמל היישוב"])

firstRow = {f"תקרה {year}": f"תקרה {year}", f"שיעור {year}": f"שיעור {year}", 'שם יישוב': 'שם יישוב', 'סמל היישוב': 'סמל היישוב'}

dfToCSV.loc[-1] = firstRow
dfToCSV.index = dfToCSV.index + 1
dfToCSV = dfToCSV.sort_index()

for table in tables:
    df = table.df
    df.columns = [f"תקרה {year}", f"שיעור {year}", "שם יישוב", "סמל היישוב"]

    df["שם יישוב"] = df["שם יישוב"].str[::-1]

    df["שם יישוב"] = df["שם יישוב"].str.replace('\n', '')

    dfToCSV = pd.concat([dfToCSV, df.iloc[1:, :]])

dfToCSV['שם יישוב'] = dfToCSV['שם יישוב'].replace({'-טלאל': 'טל-אל', 'נהרייה': 'נהריה'})

if not os.path.exists(sys.argv[2]):
    print("Invalid path!")
else:
    dfToCSV.to_csv(
        sys.argv[2],
        header=False, index=False, encoding='utf-8-sig')
