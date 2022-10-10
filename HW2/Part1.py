# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 20:26:46 2020

@author: annorm
"""

import math
radius = input("Enter the gum ball radius (in.) => ")
print(radius)
radius = float(radius)
sales = int(input("Enter the weekly sales => "))
print(sales)

target_sales = math.ceil(sales*1.25)
edge = math.ceil(target_sales**(1/3))
diameter = radius*2
side = edge*diameter
total = edge**3
extra = total-target_sales


def find_volume_sphere(radius):
    return (((radius**3)*4*math.pi)/3)
def find_volume_cube(side):
    return ((side**3))

print(" ")
print("The machine needs to hold", edge, "gum balls along each edge.")
print("Total edge length is {:.2f}".format(side),"inches.")
print("Target sales were", str(target_sales)+", but the machine will hold", extra, "extra gum balls.")
waste = find_volume_cube(side) - (find_volume_sphere(radius)*target_sales)
wasted = find_volume_cube(side) - (find_volume_sphere(radius)*total)
print("Wasted space is {:.2f} cubic inches with the target number of gum balls,".format(waste), "\nor {:.2f} cubic inches if you fill up the machine.".format(wasted))
