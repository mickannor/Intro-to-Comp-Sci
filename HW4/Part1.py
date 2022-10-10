# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 13:38:15 2020

@author: annorm
"""
""" PROGRAM THAT DETERMINES THE STRENGTH OF A PASSWORD BASED OFF LENGTH AND SPECIAL CHARACTERS"""

import hw4_util


def password_strength(password):
    score = 0
    
    #1 SCORE BASED ON LENGTH
    if len(password) == 6 or len(password) == 7:
        score += 1
        print("Length: +1")
    elif len(password) >= 8 and len(password) <= 10:
        score += 2
        print("Length: +2")
    elif len(password) > 10:
        score += 3
        print("Length: +3")
        
    #2 SCORE BASED ON CASE
    lower_letters= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    cap_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    i = 0
    lower_count = 0
    j = 0
    cap_count = 0
    
    while i < len(lower_letters):
        lower_count += password.count(lower_letters[i])
        i += 1
    
    while j < len(cap_letters):
        cap_count += password.count(cap_letters[j])
        j += 1
    
    if lower_count > 1:
        lower_count = 2
    if cap_count > 1:
        cap_count = 2
    
    if lower_count + cap_count == 2 or cap_count + lower_count == 3:
        score += 1
        print("Cases: +1")
    elif lower_count + cap_count == 4:
        score += 2
        print("Cases: +2")
            
    
    #3 SCORE BASED ON DIGITS
    digit_count = 0
    digit = 0
    while digit <= 9:
        digit_count += password.count( str(digit) )
        digit += 1
        
    if digit_count == 1:
        score += 1
        print("Digits: +1")
    elif digit_count >1:
        score += 2
        print("Digits: +2")
        
    #4 SCORE BASED ON PUNCTUATION
    char1_count = 0
    char1_count += password.count("!")
    char1_count += password.count("@")
    char1_count += password.count("#")
    char1_count += password.count("$")
    if char1_count >= 1:
        score += 1
        char1_count = 1
        
    char2_count = 0
    char2_count += password.count("%")
    char2_count += password.count("^")
    char2_count += password.count("&")
    char2_count += password.count("*")
    if char2_count >= 1:
        score += 1
        char2_count = 1
        
    if char1_count + char2_count == 2:
        print("!@#$: +1")
        print("%^&*: +1")
    elif char1_count + char2_count == 1:
        if char1_count == 1:
            print("!@#$: +1")
        if char2_count == 1:
            print("%^&*: +1")
        
        
    #5 SCORE BASED ON NY LICENSE
    if password.isalnum() == True:
        number = 0
        stop = "False"
        while number <= 9:
            pos = password.find( str(number) )
            if  0 <= pos and pos < len(password) and stop == "False":
                if password[(pos-3):pos].isalpha() == True and password[pos:(pos+4)].isnumeric() == True:
                    score -= 2
                    print("License: -2")
                    stop = "True"
            number += 1
                    
    #6 SCORE BASED ON RARITY
    common_passwords = hw4_util.part1_get_top()
    i = 0
    common_password=[]
    while i < len(common_passwords):
        if password.lower() == common_passwords[i]:
            score -= 3
            common_password.append(password)
        i += 1
       
    if len(common_password) > 0:    
        print("Common: -3")
        
    print("Combined score:", score)
    
    if score <= 0:
        print("Password is rejected")
    elif score == 1 or score == 2:
        print("Password is poor")
    elif score == 3 or score == 4:
        print("Password is fair")
    elif score == 5 or score == 6:
        print("Password is good")
    elif score >= 7:
        print("Password is excellent")
    
if __name__ == "__main__":
    password = input("Enter a password => ")
    print(password)
    
password_strength(password)
