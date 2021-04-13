#CSV to Parquet
import pandas as pd
from os import listdir
from os.path import isfile, join

fileList = [f for f in listdir('SOURCE DIRECTORY') if isfile(join('SOURCE DIRECTORY', f))]

for infile in fileList:
    df = pd.read_csv('SOURCE DIRECTORY' + infile)
    df.to_parquet('OUTPUT DIRECTORY' + infile[:-4] + '.parquet')
