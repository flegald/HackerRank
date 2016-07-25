#!/bin/python3

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

def kanga_match(x1, v1, x2, v2):
    if x1 < x2 and v1 <= v2:
        print('NO')
        return
    if x1 < x2:
        first = x1
        first_speed = v1
        second = x2
        second_speed = v2
    elif x2 < x1:
        first = x2
        first_speed = v2
        second = x1
        second_speed = v1
    else:
        print('YES')
        return
    while first < second:
        first += first_speed
        second += second_speed
        if first == second:
            print('YES')
            return
    print('NO')
        
            
kanga_match(x1, v1, x2, v2)