# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:25:36 2020

@author: annorm
"""
# HW3 PART 1

import syllables


paragraph = input("Enter a paragraph => ")
print(paragraph)
#FIND ASL
sentences=paragraph.split(".")

i=0
total=0
while i <= len(sentences)-1:
    total+=len( sentences[i].split() )
    i+=1

ASL=total/(len(sentences)-1)

#FIND PHW
words= paragraph.split()

word_count=[]
i=0

    #LIST OF WORDS WITH THREE OR MORE SYLLABLES

while i <= len(words)-1:
    if syllables.find_num_syllables(words[i]) >= 3:
        word_count.append(words[i])
    i+=1
        

    #REMOVING WORDS THAT CONTAIN HYPHENS AND END WITH "ES" OR "ED"
i=0
while i <= len(word_count)-1:
    j=0
    while j <= len(word_count[i])-1:
        if word_count[i][j]== "-" :
            word_count.pop(i)
        elif word_count[i][-1]=="s" and word_count[i][-2]=="e":
            word_count.pop(i)
        elif word_count[i][-1]=="d" and word_count[i][-2]=="e":
            word_count.pop(i)
        j+=1
    i+=1

PHW=( ( len(word_count) / len(words) )*100 )



#FIND ASYL
total_syllables=0
i=0

while i <= len(words)-1:
    total_syllables+=syllables.find_num_syllables(words[i])
    i+=1
    
ASYL=total_syllables/len(words)

#FIND GFRI
GFRI= 0.4*(ASL + PHW)

#FIND FKRI
FKRI= 206.835 - 1.015 * ASL - 86.4 * ASYL

#PRINT STATEMENTS
print("Here are the hard words in this paragraph: ")
print(word_count)

print("Statistics: ASL:{:.2f} PHW:{:.2f}% ASYL:{:.2f}".format(ASL, PHW, ASYL) )
    
print("Readability index (GFRI): {:.2f}".format(GFRI) )
print("Readability index (FKRI): {:.2f}".format(FKRI) )

