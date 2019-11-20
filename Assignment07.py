# ------------------------------------------------- #
# Title: Assignment07
# Description: Assignment 07 - pickling and error handing
# ChangeLog: (Who, When, What)
# Tony Le,<11.18.2019>,Created Script
# ------------------------------------------------- #

import pickle  # This imports code from another code file

# Data -------------------------------------------- #

file_Name = "Assignment07.txt"
a = ['Value 1','Value 2','Value 3']

# Processing -------------------------------------- #

fileObject = open(file_Name,'wb') # Open the file for writing
pickle.dump(a, fileObject) # This writes the object "a" to the file named 'Assignment07.txt'
fileObject.close() # This closes the fileObject

fileObject = open(file_Name,'rb') #Open the file to read from 'Assignment07.txt'
b = pickle.load(fileObject) # load the object from the file into var b
fileObject.close() # This closes the fileObject

# Presentation ------------------------------------ #

try:
    print("a is written as: " + a + " in binary file")
    print("b is read as: " + str(b) + " from a binary file")
except:
    print('Error: Types do not match!\n')
else:
    print('No exceptions!')

try:
    print('Attempt #2: ')
    print("a is written as: " + str(a) + " in binary file")
    print("b is read as: " + str(b) + " from a binary file\n")
except:
    print('Error: Types do not match!\n')
else:
    print('No exceptions!')

