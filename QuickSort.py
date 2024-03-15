# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 23:00:52 2023

@author: maxco
G number: 20997755
"""

from GlobalCounter import IncrementCountComparison

def quickSort(arr):
    length = int(len(arr))
    if(length <= 1):
        return arr
    pivot = int(arr[length // 2]) # middle value
    lessThanArray = []
    moreThanArray = []
    for i in range(length - 1):
        if(pivot < arr[i]):
            lessThanArray.append(arr[i])
            IncrementCountComparison()
        else:
            moreThanArray.append(arr[i])
            IncrementCountComparison()
            #global count_comparison
            #count_comparison += 1
    return quickSort(moreThanArray) + [pivot] + quickSort(lessThanArray)

