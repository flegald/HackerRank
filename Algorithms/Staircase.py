#!/bin/python3

import sys


n = int(input().strip())

def staircase(num):
    space_count = num - 1
    stair_count = 1
    for i in range(num):
        space = " " * space_count
        stair = "#" * stair_count
        print(space + stair)
        space_count -= 1
        stair_count += 1
    
staircase(n)
        