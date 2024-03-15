# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 14:28:32 2023

@author: maxco
G number: 20997755
"""
from GlobalCounter import IncrementCountComparison

def selectionSort(arr):
    # find smallest value against all values, then place it in the net index
    arrayLength = int(len(arr))
    
    # range from start to end of array
    for i in range(0, arrayLength - 1):
        # we assume current index is smallest
        smallestIndex = i
        # go through remainig elements that is not the smallest element, and compare them all
        for j in range(i + 1, arrayLength):
            IncrementCountComparison()
            # compare value in array to next value at position j
            if(arr[j] < arr[smallestIndex]):
                smallestIndex = j
        # this swaps the elemts in the array if the value is not already the current index value
        if(smallestIndex != i):
            temp = arr[i]
            arr[i] = arr[smallestIndex]
            arr[smallestIndex] = temp
            
    return arr