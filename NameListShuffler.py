# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 15:10:30 2024

@author: maxco
"""

import Constant
import SelectionSort
import random

def read_file(fileName):
    with open(fileName, 'r') as file: 
         #reads at the specific file location
         lines = file.readlines() # copy of names
         return lines
         
def readTruncate_file(fileName):
    with open(fileName, 'r+') as file: 
        lines = file.readlines() # copies all of file lines onto a string
        file.seek(0) # moves the 'file cursor' to the start of file
        file.truncate() # Chops the file, basically empty now.
        
        if len(lines) >= Constant.TRIMVALUE:
            file.writelines(lines[:Constant.TRIMVALUE]) # uses array slicing
        print(f"number of lines for {fileName} is: ", len(lines)) # output number of lines       
        
     
def fullNameShuffle(firstNames, lastNames):
    # Assuming both lists have the same length of 4000
    # Before shuffling, we need to shuffle the last names, to ensure each full name is random
    shuffledLastNames = lastNames
    random.shuffle(shuffledLastNames)
    
    # These are needed (name.strip()) to get rid of an issue where at the end of each first or last name
    # there was a "\n" messing the format of the fullNames.txt file
    firstNames = [name.strip() for name in firstNames]
    shuffledLastNames = [name.strip() for name in shuffledLastNames]
    
    # f-Strings f"" are simply creating a new string using variables too.
    # Zips are used to iterate over multiple lists producing 'tuples' - pairing the first and last names
    # Tuples are like lists, but cannot be edited after creation (immutable)  
    fullNames = [first + " " + last + "\n" for first, last in zip(firstNames, shuffledLastNames)]
    # so we should create a string of "Aaren Auberg" for example.
    
    with open('fullNames.txt', 'w') as file:
        for fullName in fullNames:
            file.write(fullName)
    
    return fullNames


### Name List Shuffler 1 ###

# 1a) Open files and trim the lines to only have 4000 lines of data.
# 1b) Merge Random name arrays to FullNames -> Create .txt file.
# 1c) Then Output the LongestFullName inside the list.

# I want to create 2 arrays that can store the data of firstNames and lastNames
   
# used array slicing to chop the array off.    
#maximum_lines = 4000

# 1a) v2: Open files, trim to 4000 lines. Then output number of lines.
    
# open file using 'r+' is combining reading, truncating 
# and writing into a single operation: 
# (alternative would be 'r' reading into file and 'w' writing into file)
# using the 'with' statement helps close the file afterwards

readTruncate_file('firstNames.txt')
readTruncate_file('lastNames.txt')

# 1b) v2: read in first and last, merge randomly together
# for example - (James Smith)

# empty strings to be pasted into
FNLines = str() 
LNLines = str()
 
# may need to use this?  all_FN_List = file.read().splitlines()


FNLines = read_file('firstNames.txt')
LNLines = read_file('lastNames.txt')  

# assuming this works...
# now merge two lists together randomly (into fullName.txt):

# Merge: 
# This function, merges the first and last names using an F-String: 
# (Formatted String), 

# Write a .txt file of fullNames, inputing all the info in:
fullNameShuffle(FNLines, LNLines)

# 1c) v1: output longest name in the fullNameShuffler
# output highest characters

# MergeSort, the length of fullnames and output largest value
# create an array of lengths of the name shuffler
fullNames = read_file('fullNames.txt')
    
# Remove newline characters from each full name
fullNames = [name.strip() for name in fullNames]

# Create an array of lengths of characters for each full name
lengths_array = [len(name) for name in fullNames]

# Sort a copy of lengths array (to not edit original array)
SelectionSort.selectionSort(lengths_array)

# print biggest num result
print("The longest full name with highest characters is: ", lengths_array[Constant.TRIMVALUE - 1])