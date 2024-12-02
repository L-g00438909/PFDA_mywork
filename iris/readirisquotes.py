# LR

import csv

FILENAME= "irisquotes.csv"
DATADIR = "../iris/"

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter="," , quoting=csv.QUOTE_NONNUMERIC)
    
    for line in reader:
        sepal_size= line['sepal_length'] * line['sepal_width']
        petal_size= line['petal_length'] * line['petal_width']
        line["sepal_area"] = sepal_size
        line["petal_area"] = petal_size
        
        print (line)

# The code reads the irisquotes.csv file and calculates the sepal and petal sizes by multiplying the length and width of each.
# The sepal and petal sizes are then appended to the line and printed.
# The code uses the csv module to read the file and perform the calculations.
# The code assumes that the file is in the specified directory and has the specified format.
# The code could be improved by adding error handling and validation for the input data.
# The code could also be optimized for performance by using more efficient data structures and algorithms.
# The code could be further enhanced by adding additional functionality, such as plotting the data or performing statistical analysis.

