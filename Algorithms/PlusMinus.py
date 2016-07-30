#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

def plus_minus(list):
    length = len(list)
    pos = 0
    neg = 0
    zero = 0
    for i in list:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1
    print(pos/length)
    print(neg/length)
    print(zero/length)
    
plus_minus(arr)