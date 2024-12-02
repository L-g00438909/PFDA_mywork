# case study of iris data set
# area of sepal and petals
# Author: LR

import csv

FILENAME= "iris.csv"  # file name is iris.csv 
DATADIR = "../iris/"   # data directory is iris 

with open (DATADIR + FILENAME, "rt") as fp:   # open the file iris.csv in read text mode 
    reader = csv.reader(fp, delimiter="," , quoting=csv.QUOTE_NONE) # read the file using csv reader. 
    
    for line in reader:                              # cant * strings need to cnvert to float
        sepal_size= float(line[0]) * float(line[1])  # sepal size is the product of sepal length and sepal width
        petal_size= float(line[2]) * float(line[3])  # petal size is the product of petal length and petal width 
        line.append(sepal_size)   # append sepal size to the line 
        line.append(petal_size)   # append petal size to the line
        print (line) 


# The code reads the iris.csv file and calculates the sepal and petal sizes by multiplying the length and width of each.
# The sepal and petal sizes are then appended to the line and printed.
# The code uses the csv module to read the file and perform the calculations.
# The code assumes that the file is in the specified directory and has the specified format.
# The code could be improved by adding error handling and validation for the input data.
# The code could also be optimized for performance by using more efficient data structures and algorithms.
# The code could be further enhanced by adding additional functionality, such as plotting the data or performing statistical analysis.
# Overall, the code provides a basic example of reading and processing CSV data in Python.

