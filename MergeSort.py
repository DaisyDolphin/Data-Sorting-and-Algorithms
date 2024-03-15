# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 14:05:32 2023

@author: maxco
G number: 20997755
"""

from GlobalCounter import IncrementCountComparison

def mergeSort(arr):
    # what exactly is a merge sort? split array in half from centre, recursion...
    # sort data, and then recombine data again
    # First check if array is one or zero elements, it should return back to an array
    
    arrayLength = int(len(arr));
    if(arrayLength <= 1): # sorted
        return arr
        # need to split the array into two different arrays through the middle.
    middle = int(arrayLength/2);
    # divide the array in the middle into two subarrays
    leftHalf = arr[0:middle];
    rightHalf = arr[middle:];
    
    leftSorted = mergeSort(leftHalf);
    rightSorted = mergeSort(rightHalf);

    # merge sorted arrays
    
    return MergeTwoSortedArrays(leftSorted, rightSorted);

def MergeTwoSortedArrays(arr1, arr2):
    
    # to do this, i need to comapre the first two values in each array
    # and then add the lowest onto the completed array, complete until
    # one array is empty, and then add rest of values in, then done.
    
    i = int(0); # index values
    j = int(0); 
    length1 = int(len(arr1));
    length2 = int(len(arr2));
    
    MergedArray = [];
    
    while((i < length1) and (j < length2)): # keep comparing until one array is empty
        IncrementCountComparison()
        #global count_comparison
        #count_comparison += 1
        if(arr1[i] < arr2[j]): # compares smallest value in arr1 to arr2
            MergedArray.append(arr1[i]); # if value least, add it to completed array
            i+=1 #increment index
        else:
            MergedArray.append(arr2[j]);
            j+=1;
    # we expext one array to run out of values first, so we need to check for that:
    while (i < length1): # checks if arr2 ran out of values
        MergedArray.append(arr1[i]); # adds remaining values to new array
        i+=1;
        IncrementCountComparison()
        
    while (j < length2): # checks if arr1 ran out of values
        MergedArray.append(arr2[j]); # adds remaining values to new array
        j+=1;
        IncrementCountComparison()
        
    #print ("array has been sorted!", '/n');
    return MergedArray;