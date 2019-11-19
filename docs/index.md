# Pickling and Structured Error Handling
**Dev:** *Tony Le*  
**Date:** *11.19.2019*  
**Class:** *IT FDN 100*  
**Assignment:** *07*  

## Introduction
The assignment for this week is to research and create a script that demonstrates how pickling and structured error handling works. 

## Importing pickle
The first step as shown in Listing 1 is to import Pickle’s methods into the script.

```
import pickle
```
#### Listing 1: Import Pickle

## Declaring a class
Listing 2 establishes the variables that will be used later on in the script. We define a variable that will be used to open up our file and we assign a list to a variable to be written and read.
```
file_Name = "Assignment07.txt"
a = ['Value 1','Value 2','Value 3']
```
#### Listing 2: Assigning Variables

## Processing the writing and reading of the data
The first part of the processing is shown in Listing 3. We first assign a variable that opens the file for writing with fileObject. This time, we ensure to use ‘wb’ to indicate that we are writing in binary. We then store the data away with pickle.dump and close the file.

```
fileObject = open(file_Name,'wb')
pickle.dump(a, fileObject) 
fileObject.close() 
```
#### Listing 3: Write the list to file

The script in Listing 4 opens and reads the file that has been stored in binary. With the pickle.load command, we are able to load the stored data into a variable assigned as b. 

```
fileObject = open(file_Name,'rb')
b = pickle.load(fileObject)
fileObject.close()
```
#### Listing 4: Reading the list

## Structured error handling
The presentation section is detailed in Listing 5 which also demonstrates how structured error handling works. We utilize the try, except and else commands in order to output a custom error message in the case it fails. In the script here, the first try will fail due to a type error and the second one will pass.

```
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
```
#### Listing 5: Structured error handling

## Summary
Listing 6 shows the script in its entirety and Figure 1 shows the output of the script. The output shows that it is functioning as intended with the results of the data saved in a txt file in binary. To summarize, the script begins by assignment a value to “a” in normal text as a list. This list is then written into a file in binary and the data is stored by the pickle.dump method. Afterwards, the data is read in its binary form and loaded into the variable “b” by the pickle.load method. At this point, the list is back in its original form. The output of the script shown in Figure 7 shows the text file is stored as binary data.
 
```
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
```
#### Listing 6: Full script

![Script output showing a file stored in binary](https://github.com/TonyLe2/ITFnd100--Mod07/blob/master/docs/Figure7.png "Script output showing a file stored in binary")
#### Figure 1: Script output showing a file stored in binary
