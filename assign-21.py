import xlrd

path = r"C:\Users\HP\OneDrive\Documents\data.xlsx"

wb = xlrd.open_workbook(path)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

# TO SEE ALL COLUMN NAMES
for i in range(sheet.ncols):
    print(sheet.cell_value(0, i))

# TO SEE FULL COLUMN
for i in range(sheet.nrows):
    print(sheet.cell_value(i, 0))

# TO SEE PARTICULAR ROW VALUE
print(sheet.row_values(2))

# TO PRINT TOTAL NUMBER OF COLUMN
print(sheet.ncols)

# TO PRINT TOTAL NUMBER OF ROWS
print(sheet.nrows)

# TO PRINT PARTICULAR VALUE OF ANY CELL
print(sheet.cell_value(0, 1))
