import camelot

# Read PDF file
tables = camelot.read_pdf('2.pdf', pages='all')

# Convert tables to DataFrames
dfs = [table.df for table in tables]

# Display the first few rows of each DataFrame
for i, df in enumerate(dfs):
    print(f"Table {i}:")
    print(df.head())
