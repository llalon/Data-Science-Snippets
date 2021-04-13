#Extracts tables from a .docx and outputs a CSV file for each.
from docx import Document
import pandas as pd

document = Document('SOURCE FILE')
tables = []
#Read the docx and enumerate tables from top to bottom
for index, table in enumerate(document.tables):
    df = [['' for i in range(len(table.columns))] for j in range(len(table.rows))]
    for i, row in enumerate(table.rows):
        for j, cell in enumerate(row.cells):
            df[i][j] = cell.text
        #Convert to a Pandas DataFrame -> drop the first (index) row -> write to csv
        pd.DataFrame(df).iloc[1:].to_csv('OUTPUT DIRECTORY/Table#' + str(index) + '.csv', index=False)
