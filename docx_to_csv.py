#!/usr/bin/env python

# Extracts all tables from a .docx file and outputs each table to a CSV
# Usage Example: docx_to_csv.py document.docx --output out_dir

from docx import Document
import pandas as pd

import sys
import os
import argparse
import pathlib


def doc_to_csv(file, out=pathlib.Path("./"), ind=False, head=False):
    document = Document(file)
    tables = []
    for index, table in enumerate(document.tables):
        df = [["" for i in range(len(table.columns))] for j in range(len(table.rows))]
        for i, row in enumerate(table.rows):
            for j, cell in enumerate(row.cells):
                df[i][j] = cell.text
            pd.DataFrame(df).to_csv(
                "%s/Table#%s.csv" % (str(out), str(index)), index=ind, header=head
            )


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description="Extracts tables from .docx to csv")
    argparser.add_argument(
        "filename", type=pathlib.Path, help="Sets the .Docx file to be used."
    )
    argparser.add_argument(
        "-o",
        "--output",
        action="store",
        default=pathlib.Path("./"),
        type=pathlib.Path,
        help="Sets the output folder. Defaults to the current working directory.",
    )
    argparser.add_argument(
        "-i",
        "--index",
        action="store_true",
        default=False,
        help="Adds index column to csv files.",
    )
    argparser.add_argument(
        "-r",
        "--header",
        action="store_true",
        default=False,
        help="Adds headers to csv files.",
    )

    args = argparser.parse_args(sys.argv[1:])

    FILE = args.filename
    DIR = args.output
    INDEX = args.index
    HEADER = args.header

    doc_to_csv(FILE, DIR, INDEX, HEADER)