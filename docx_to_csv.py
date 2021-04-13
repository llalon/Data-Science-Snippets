#Extracts all tables from a .docx file and outputs each table to a CSV
from docx import Document
import pandas as pd

document = Document('SOURCE FILE')
tables = []
for index, table in enumerate(document.tables):
    df = [['' for i in range(len(table.columns))] for j in range(len(table.rows))]
    for i, row in enumerate(table.rows):
        for j, cell in enumerate(row.cells):
            df[i][j] = cell.text
        pd.DataFrame(df).to_csv('OUTPUT DIRECTORY/Table#' + str(index) + '.xlsx')
