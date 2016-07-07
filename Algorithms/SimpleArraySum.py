#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

def add(list):
    sum = 0
    for i in list:
        sum += i
    print(sum)
    
add(arr)