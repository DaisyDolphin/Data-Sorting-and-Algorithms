# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 19:32:37 2024

@author: maxco
G number: 20997755
"""

import Constant
import MergeSort
import SelectionSort
import QuickSort
from GlobalCounter import GetNResetCountComparison
#import firstNames.txt
#import lastNames.txt
#import numpy as np
#from numpy.random import seed
from numpy.random import randint # random ints
#import random
import time
from datetime import datetime
dt = datetime.now()
import matplotlib.pyplot as plt

### functions ###

def UniqueRandomArray(numOfElements, lowerRange, higherRange):
    # create the array 
    arrayName = []
    # will continue to create the array until num of elements reached
    while(len(arrayName) < numOfElements):
        newValue = randint(lowerRange, higherRange) # creating 1 element first to check if its unique

        # check if inside the array is a unique value
        if(newValue not in arrayName):
            arrayName.append(newValue)
            # if value is in the array, ignore
            # else append into the array
    return arrayName

def ReturnTestValue():
    return Constant.RANDOM_ARR_VAL1
    #return 10

def StartTimer():
    start = time.perf_counter()
    return start

def EndTimer():
    end = time.perf_counter()
    return end

def Sort(sortType, UnsortedArray):
    # gets current time in seconds for Sort (print to 4dp)
    start = StartTimer()
    if(sortType == "Selection"):
        # at some point, the sorted array here is replacing the unsorted one.
        SortedArray = SelectionSort.selectionSort(UnsortedArray)  
    elif(sortType == "Merge"):
        SortedArray = MergeSort.mergeSort(UnsortedArray)
    elif(sortType == "Quick"):
        SortedArray = QuickSort.quickSort(UnsortedArray)   
    end = EndTimer()
    seconds = end - start
    #print(SortedArray)
    length = len(SortedArray)
    print("For the ", sortType, "sort, with ", length, " values, it takes: ", round(seconds, Constant.decimalPlace), " seconds. ");
    print("Number of swaps: ", GetNResetCountComparison())
    # coords can be used in the graph formed later
    coords = [seconds, length]
    return coords

### RNG Data Sorter (Sorting Algorithms) ###

# 2a) create arrays of 100, 1000, 10000 elements (random values from 100000 to 999999)

# Random array but creates repeated values
RandomArray1 = UniqueRandomArray(Constant.RANDOM_ARR_VAL1, Constant.NUM_LOWER_RANGE, Constant.NUM_HIGHER_RANGE)
RandomArray2 = UniqueRandomArray(Constant.RANDOM_ARR_VAL2, Constant.NUM_LOWER_RANGE, Constant.NUM_HIGHER_RANGE)
RandomArray3 = UniqueRandomArray(Constant.RANDOM_ARR_VAL3, Constant.NUM_LOWER_RANGE, Constant.NUM_HIGHER_RANGE)

# 2b) sort using each 3 algorithms
# 2c) AND use .copy() on all array

#coordinates in Sort output = [seconds, element amount]

# 100 set
quick_coords1 = Sort("Quick", RandomArray1.copy())
merge_coords1 = Sort("Merge", RandomArray1.copy())
selection_coords1 = Sort("Selection", RandomArray1.copy())
print('\n')
# 1000 set
quick_coords2 = Sort("Quick", RandomArray2.copy())
merge_coords2 = Sort("Merge", RandomArray2.copy())
selection_coords2 = Sort("Selection", RandomArray2.copy())
print('\n')
# 10000 set
quick_coords3 = Sort("Quick", RandomArray3.copy())
merge_coords3 = Sort("Merge", RandomArray3.copy())
selection_coords3 = Sort("Selection", RandomArray3.copy())
print('\n')

#timeset = [seconds, element length], so [0] gives the time amount
# the '[0]' and '[1]' aren't magic numbers because, 
# they're needed in thsi format for how i ouput results from the Sort function
quick_timeset = [quick_coords1[0], quick_coords2[0], quick_coords3[0]]
merge_timeset = [merge_coords1[0], merge_coords2[0], merge_coords3[0]]
selection_timeset = [selection_coords1[0], selection_coords2[0], selection_coords3[0]]

quick_lengthset = [quick_coords1[1], quick_coords2[1], quick_coords3[1]]
merge_lengthset = [merge_coords1[1], merge_coords2[1], merge_coords3[1]]
selection_lengthset = [selection_coords1[1], selection_coords2[1], selection_coords3[1]]

# 3) Create graphs - matplot.lib
# to plot i need a set of x coords and y coords, if i input just a coordinate set, its messes it up
plt.plot(quick_timeset, quick_lengthset, label="Quick Sort")
plt.plot(merge_timeset, quick_lengthset, label="Merge Sort")
plt.plot(selection_timeset, quick_lengthset, label="Selection Sort")
plt.legend(loc="upper left")
plt.title("A graph to compare the Big O Notation of 3 different sorting algorithms.")
plt.xlabel("Time taken (s, seconds)")
plt.ylabel("Number of elements (n)")
plt.grid()
plt.show()