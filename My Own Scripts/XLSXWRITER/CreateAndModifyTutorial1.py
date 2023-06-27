# XlsxWriter can only create new files. It cannot read or modify existing files.

import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

expenses = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],
)

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for item, cost in (expenses):
    worksheet.write(row, col + 1, item)
    worksheet.write(row, col + 2, cost)
    row += 1

# Write a total using a formula.
worksheet.write(row, col + 1, 'Total')
worksheet.write(row, col + 2, '=SUM(C1:C4)')

workbook.close()