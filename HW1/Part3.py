# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 17:54:24 2020

@author: annorm
"""

frame=(input("Enter frame character ==> "))
str(frame)
print(frame)
height_num=int((input("Height of box ==> ")))
print(height_num)
width_num=int((input("Width of box ==> ")))
print(width_num)
print("")
print("Box:")

top_down=frame*width_num
count=(height_num-3)//2
count_round=height_num-(3+count)
mid=frame+" "*(width_num-2)+frame+"\n"
width_str=str(width_num)
height_str=str(height_num)
dimension=width_str+"x"+height_str
dim=len(dimension)
beginning=frame+" "*int((((width_num-2))//4))+dimension
end=" "*(width_num-len(beginning)-1)+frame
middle=beginning+end


print(top_down,mid*count,sep="\n",end="")
print(middle,mid*count_round,sep="\n",end="")
print(top_down)
