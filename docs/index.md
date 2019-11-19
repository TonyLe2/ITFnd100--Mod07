<div align="center"> # Pickling and Structured Error Handling </div>
**Dev:** *Tony Le*  
**Date:** *11.19.2019*  
**Class:** *IT FDN 100  
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

The script in Figure 4 opens and reads the file that has been stored in binary. With the pickle.load command, we are able to load the stored data into a variable assigned as b. 
 
Figure 4: Reading the list

Structured error handling
The presentation section is detailed in Figure 5 which also demonstrates how structured error handling works. We utilize the try, except and else commands in order to output a custom error message in the case it fails. In the script here, the first try will fail due to a type error and the second one will pass.
 
Figure 5: Structured error handling
Summary
Figure 6 shows the script in its entirety and Figure 7 shows the output of the script. The output shows that it is functioning as intended with the results of the data saved in a txt file in binary. To summarize, the script begins by assignment a value to “a” in normal text as a list. This list is then written into a file in binary and the data is stored by the pickle.dump method. Afterwards, the data is read in its binary form and loaded into the variable “b” by the pickle.load method. At this point, the list is back in its original form. The output of the script shown in Figure 7 shows the text file is stored as binary data.
 
Figure 6: Full script


 
Figure 7: Script output showing a file stored in binary




```
# ------------------------------------------------- # # Title: Listing 13
# Description: A try-catch with manually raised errors # ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #

try:
    new_file_name = input("Enter the name of the file you want to make: ") 
    if new_file_name.isnumeric():
        raise Exception('Do not use numbers for the file\'s name') 
except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
```
#### Listing 13

![Results of Listing 13](https://github.com/TonyLe2/ITFnd100--Mod07/blob/master/docs/Figure13.png "Results of Listing 13")

#### Figure 13. The results of Listing 13.
