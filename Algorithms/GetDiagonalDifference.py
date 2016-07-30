#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

def difference(v):
    diff = 0
    v_len = len(v)
    for idx in xrange(v_len):
        diff += v[idx][idx]
        diff -= v[idx][v_len-idx-1]
 
    return abs(diff)    
         
print difference(a)