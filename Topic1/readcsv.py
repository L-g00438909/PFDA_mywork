# read csv file 
# Author: LR

import csv

FILENAME = 'data.csv'
DATADIR = 'Where did you get it?'

with open(DATADIR + FILENAME, 'rt') as fp: #fp is a file pointer 
    reader = csv.DictReader(fp, delimiter=',', quoting=csv.QUOTE_NONE) 
    for line in reader:
        print(line)