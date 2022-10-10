# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:41:44 2020

@author: annorm
"""
import math

minutes=int(input("Minutes ==> "))
print(minutes)
seconds=input("Seconds ==> ")
print(seconds)
seconds=int(seconds)
miles=input("Miles ==> ")
print(miles)
miles=float(miles)
target_miles=input("Target Miles ==> ")
print(target_miles,end="\n\n")
target_miles=float(target_miles)

pace_minutes=int(((((minutes*60)+seconds)/miles)//60))
pace_seconds=int((((minutes*60)+seconds)/miles)%60)
print("Pace is",pace_minutes,"minutes and",pace_seconds,"seconds per mile.")

speed=float(((miles/((minutes*60)+seconds)*60)*60))
print("Speed is {:.2f} miles per hour.".format(speed))

runtime_minutes=int(((((pace_minutes*60)+pace_seconds)*target_miles)//60))
runtime_seconds=math.ceil((((pace_minutes*60)+pace_seconds)*target_miles)%60)
print("Time to run the target distance of {:.2f} miles is".format(target_miles),runtime_minutes,"minutes and",runtime_seconds,"seconds.")
