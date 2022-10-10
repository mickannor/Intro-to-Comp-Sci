# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 19:36:04 2020

@author: annorm
"""

def parsing_file(file,stop):
    newlist = []
    for words in file:
        for letters in words:
            if letters.isalpha() == False:
                words = words.replace(letters, "")
        words = words.lower()
        if words not in stop:
            newlist.append(words)
        if words == '':
            newlist.remove(words)
    return(newlist)


file1 = input("Enter the first file to analyze and compare ==> ")
print(file1)
file2 = input("Enter the second file to analyze and compare ==> ")
print(file2)
max_sep = int(input("Enter the maximum separation between words in a pair ==> "))
print(max_sep)
print("")


#OPENING EACH SEPARATE FILE 
s = open("stop.txt")
s = s.read()
s_list = s.split()
x1 = open(file1)
x1 = x1.read()
x = x1.split()
x2 = open(file2)
x2 = x2.read()
xx = x2.split()


#PARSING EACH FILE IN THE FUNCTION
stop = set(parsing_file(s_list,set()))
x = parsing_file(x,stop)
x1_set = set(x)
xx = parsing_file(xx,stop)
x2_set = set(xx)


#TAKING OUT THE STOP FROM EACH AND MAINTANING THE ORDER
x1_list = list(x1_set.difference(stop))
for words in x:
    if words not in x1_list:
        x.remove(words)
x2_list = list(x2_set.difference(stop))
for words in xx:
    if words not in x2_list:
        xx.remove(words)


#FIND THE AVERAGE WORD LENGTH AND THE RATIO OF UNIQUE TO TOTAL WORDS
x_total = 0
for words in x:
    x_total += len(words)
x_avr = x_total/len(x)

xx_total = 0
for words in xx:
    xx_total += len(words)
xx_avr = xx_total/len(xx)

print("Evaluating document" , file1)
print("1. Average word length: {:.2f}".format(x_avr))
print("2. Ratio of distinct words to total words:" , "{:.3f}".format(len(x1_list)/ len(x)))
print("3. Word sets for document", file1 + ":")


#PRINTING THE LENGTH OF EACH WORD
i = 0
xmax_len = []
while i < len(x)-1: 
    if len(x[i+1]) > len(x[i]):
        xmax_len.append(len(x[i+1]))
    i += 1
        
i = 1
xword_length= []
while i <= max(xmax_len):
    count = ""
    xword_length.append(set())
    z=0
    for words in x:
        if len(words) == i:
            xword_length[i-1].add(words)
            z += 1
            count = " " + count + " " + words
    if len(set(count.split())) <= 6:
        z = len(set(count.split()))
        count = str(sorted(set(count.split())))
        count = count.rstrip("']").lstrip("['").replace("'",'',100).replace(",",'',100)
        if count != "":
            count = " " + count
        print("{:4d}".format(i) + ":" + "{:4d}".format(z) + ":" + count)
    elif len(set(count.split())) > 6:
        z = len(set(count.split()))
        count = sorted(set(count.split()))
        print("{:4d}".format(i) + ":" + "{:4d}".format(z) + ":" , count[0], count[1], count[2], "...", count[-3], count[-2], count[-1])
    i += 1


#DETERMINING PAIRS
print("4. Word pairs for document", file1)
i = 1
pairs_x = []
while i <= len(x)-1:
    c = 1
    while c <= max_sep:
        if i-c < 0:
            break
        pairs_x.append(tuple(sorted((x[i], x[i-c]))))
        c += 1 
    i += 1
pairs_x1 = pairs_x
pairs_x = sorted(list(set(pairs_x)))

print(" ", len(pairs_x), "distinct pairs")
s = 0
while s < len(pairs_x)-1:
    if len(pairs_x) <= 4:
        print(" ", pairs_x[s][0], pairs_x[s][1])
        s += 1
    elif 5 < len(pairs_x) < 11:
        s = 0
        while s <= 4:
            print(" ", pairs_x[s][0], pairs_x[s][1])
            s += 1
        if s == 5:
            print("  ...")
            s += 1
        if s > 5:
            print(" ", pairs_x[s][0], pairs_x[s][1])
            s += 1
    elif len(pairs_x) >= 11:
        s = 0
        while s <= 4:
            print(" ", pairs_x[s][0], pairs_x[s][1])
            s += 1
        if s == 5:
            print("  ...")
            s += 1
        if s > 5:
            print(" ", pairs_x[-5][0], pairs_x[-5][1])
            print(" ", pairs_x[-4][0], pairs_x[-4][1])
            print(" ", pairs_x[-3][0], pairs_x[-3][1])
            print(" ", pairs_x[-2][0], pairs_x[-2][1])
            print(" ", pairs_x[-1][0], pairs_x[-1][1])
            s = len(pairs_x)
print("5. Ratio of distinct word pairs to total: {:.3f}".format(len(pairs_x)/len(pairs_x1)))



print("")
print("Evaluating document" , file2)
print("1. Average word length: {:.2f}".format(xx_avr))
print("2. Ratio of distinct words to total words:" , "{:.3f}".format(len(x2_list)/ len(xx)))


#PRINTING THE LENGTH OF EACH WORD
print("3. Word sets for document", file2 + ":")
i = 0
xxmax_len = []
while i < len(xx)-1: 
    if len(xx[i+1]) > len(xx[i]):
        xxmax_len.append(len(xx[i+1]))
    i += 1
        
i = 1
xxword_length= []
while i <= max(xxmax_len):
    count = ""
    xxword_length.append(set())
    z = 0
    for words in xx:
        if len(words) == i:
            xxword_length[i-1].add(words)
            z += 1
            count = " " + count + " " + words
    if len(set(count.split())) <= 6:
        z = len(set(count.split()))
        count = str(sorted(set(count.split())))
        count = count.rstrip("']").lstrip("['").replace("'",'',100).replace(",",'',100)
        if count != "":
            count = " " + count
        print("{:4d}".format(i) + ":" + "{:4d}".format(z) + ":" + count)
    elif len(set(count.split())) > 6:
        z = len(set(count.split()))
        count = sorted(set(count.split()))
        print("{:4d}".format(i) + ":" + "{:4d}".format(z) + ":" , count[0], count[1], count[2], "...", count[-3], count[-2], count[-1])
    i += 1

#DETERMINING PAIRS
print("4. Word pairs for document", file2)
i = 1 
pairs_xx = []
while i <= len(xx)-1:
    c = 1
    while c <= max_sep:
        if i - c < 0:
            break
        pairs_xx.append(tuple(sorted((xx[i], xx[i-c]))))
        c += 1 
    i += 1
pairs_x2 = pairs_xx
pairs_xx = sorted(list(set(pairs_xx)))
print(" ", len(pairs_xx), "distinct pairs")

s = 0
while s < len(pairs_xx)-1:
    if len(pairs_xx) <= 4:
        print(" ", pairs_xx[s][0], pairs_xx[s][1])
        s += 1
    elif 5 < len(pairs_xx) < 11:
        s = 0
        while s <= 4:
            print(" ", pairs_xx[s][0], pairs_xx[s][1])
            s += 1
        if s == 5:
            print("  ...")
            s += 1
        if s > 5:
            print(" ", pairs_xx[s][0], pairs_x[s][1])
            s += 1
    elif len(pairs_xx) >= 11:
        s = 0
        while s <= 4:
            print(" ", pairs_xx[s][0], pairs_xx[s][1])
            s += 1
        if s == 5:
            print("  ...")
            s += 1
        if s > 5:
            print(" ", pairs_xx[-5][0], pairs_xx[-5][1])
            print(" ", pairs_xx[-4][0], pairs_xx[-4][1])
            print(" ", pairs_xx[-3][0], pairs_xx[-3][1])
            print(" ", pairs_xx[-2][0], pairs_xx[-2][1])
            print(" ", pairs_xx[-1][0], pairs_xx[-1][1])
            s = len(pairs_xx)
print("5. Ratio of distinct word pairs to total: {:.3f}".format(len(pairs_xx)/len(pairs_x2)))

print("")
print("Summary comparison")
if x_avr > xx_avr:
    print("1.", file1, "on average uses longer words than", file2)
else:
    print("1.", file2, "on average uses longer words than", file1)
print("2. Overall word use similarity: {:.3f}".format(len(set(x).intersection(set(xx)))/len(set(x).union(set(xx)))))

print("3. Word use similarity by length:")
if len(xword_length) > len(xxword_length):
    t = 0
    while t < len(xword_length):
        if t <= len(xxword_length)-1:
            if len(xword_length[t]) == 0 and len(xxword_length[t]) == 0:
                print("{:4d}".format(t+1) + ":", "{:.4f}".format(0))
            else:
                print("{:4d}".format(t+1) + ":", "{:.4f}".format(len(xword_length[t].intersection(xxword_length[t]))/len(xword_length[t].union(xxword_length[t]))))
        elif t > len(xxword_length)-1:
            print("{:4d}".format(t+1) + ":", "{:.4f}".format(0))
        t += 1
elif len(xxword_length) > len(xword_length):
    t = 0
    while t < len(xxword_length):
        if t <= len(xword_length)-1:
            if len(xxword_length[t]) == 0 and len(xword_length[t]) == 0:
                print("{:4d}".format(t+1) + ":", "{:.4f}".format(0))
            else:
                print("{:4d}".format(t+1) + ":", "{:.4f}".format(len(xword_length[t].intersection(xxword_length[t]))/len(xword_length[t].union(xxword_length[t]))))
        elif t > len(xword_length)-1:
            print("{:4d}".format(t+1) + ":", "{:.4f}".format(0))
        t += 1
else:
    t = 0
    while t < len(xword_length):
        if len(xword_length[t]) == 0 and len(xxword_length[t]) == 0:
            print("{:4d}".format(t+1) + ":", "{:.4f}".format(0))
        else:
            print("{:4d}".format(t+1) + ":", "{:.4f}".format(len(xword_length[t].intersection(xxword_length[t]))/len(xword_length[t].union(xxword_length[t]))))
        t += 1
        
print("4. Word pair similarity: {:.4f}".format(len(set(pairs_x).intersection(set(pairs_xx)))/len(set(pairs_x).union(set(pairs_xx)))))
