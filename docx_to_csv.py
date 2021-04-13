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
        #Convert to a Pandas DataFrame then write to CSV, dropping index row and column
        pd.DataFrame(df).to_csv('OUTPUT DIRECTORY/Table#' + str(index) + '.csv', header=False, index=False)
