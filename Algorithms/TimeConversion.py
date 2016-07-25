#!/bin/python3

import sys


time = input().strip()

def convert_time(stand):
    segs = stand.split(':')
    milt_time = ""
    if 'AM' in stand:
        if segs[0] == '12':
            segs[0] = "00"
            for i in segs:
                milt_time += i + ':'
            print(milt_time[:-3])
        else:
            print(stand[:-2])
    else:
        if segs[0] == "12":
            print(stand[:-2])
            return
        segs[0] = int(segs[0]) + 12
        segs[0] = str(segs[0])
        for i in segs:
            milt_time += i + ":"
        print(milt_time[:-3])
        
convert_time(time)