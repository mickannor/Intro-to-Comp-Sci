# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:42:15 2020

@author: annorm
"""
message = input("Enter a string to encode ==> ")
print(message)
print(" ")
word = message

def encrypt(word):
    word = word.replace(" a","%4%")
    word = word.replace("he","7!")
    word = word.replace("e","9(*9(")
    word = word.replace("y","*%$")
    word = word.replace("u","@@@")
    word = word.replace("an","-?")
    word = word.replace("th","!@+3")
    word = word.replace("o","7654")
    word = word.replace("9","2")
    encryted_word = word.replace("ck","%4")
    return(encryted_word)
x = encrypt(word)
print("Encrypted as ==>", x)
print("Difference in length ==>", len(x)-len(message))

def decrypt(word):
    word = word.replace("%4","ck")
    word = word.replace("2","9")
    word = word.replace("7654","o")
    word = word.replace("!@+3","th")
    word = word.replace("-?","an")
    word = word.replace("@@@","u")
    word = word.replace("*%$","y")
    word = word.replace("9(*9(","e")
    word = word.replace("7!","he")
    decrypted_word = word.replace("%4%"," a")
    return(decrypted_word)
y = decrypt(x)
print("Deciphered as ==>", y)

encrypt(word)
decrypt(word)

if y == message:
    print("Operation is reversible on the string.")
else:
    print("Operation is not reversible on the string.")
