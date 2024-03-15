# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:30:30 2024

@author: maxco
G number: 20997755
"""

### global ###

# comparison counter
g_count_comparison  = 0

def IncrementCountComparison():
    # increments the count comparison, is used in the sort functions
    global g_count_comparison
    g_count_comparison += 1
    
def GetNResetCountComparison():
    # this function outputs the count comparison 
    # as well as resets the value to zero after its use
    global g_count_comparison
    temp_count = g_count_comparison
    g_count_comparison = 0 # resetting the count
    return temp_count
