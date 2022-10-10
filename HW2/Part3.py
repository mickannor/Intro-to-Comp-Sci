# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:40:05 2020

@author: annorm
"""
sentence = input("Enter a sentence => ")
print(sentence)
sentence = sentence.lower()

def number_happy(sentence):
    sentence.count("excellent")
    sentence.count("Excellent")
    sentence.count("good")
    sentence.count("Good")
    sentence.count("smile")
    sentence.count("Smile")
    sentence.count("laugh")
    sentence.count("Laugh")
    sentence.count("happiness")
    sentence.count("Happiness")
    sentence.count("love")
    sentence.count("Love")

happy_count = (sentence.count("excellent")+sentence.count("Love")+sentence.count("Happiness")+sentence.count("Excellent")+sentence.count("Good")+sentence.count("good")+sentence.count("smile")+sentence.count("Smile")+sentence.count("laugh")+sentence.count("Laugh")+sentence.count("love")+sentence.count("happiness"))

def number_sad(sentence):
    sentence.count("horrible")
    sentence.count("Horrible")
    sentence.count("sad")
    sentence.count("Sad")
    sentence.count("bad")
    sentence.count("Bad")
    sentence.count("terrible")
    sentence.count("Terrible")
    sentence.count("problem")
    sentence.count("Problem")
    sentence.count("hate")
    sentence.count("Hate")

sad_count = (sentence.count("horrible")+sentence.count("Hate")+sentence.count("Problem")+sentence.count("Terrible")+sentence.count("Bad")+sentence.count("Sad")+sentence.count("Horrible")+sentence.count("sad")+sentence.count("bad")+sentence.count("terrible")+sentence.count("problem")+sentence.count("hate"))

number_happy(sentence)
number_sad(sentence)

if happy_count>sad_count:
    print("Sentiment:", "+" * happy_count, "\nThis is a happy sentence.")
elif happy_count == sad_count:
    print("Sentiment: " + "+" * happy_count + "-" * sad_count, "\nThis is a neutral sentence.")
elif sad_count>happy_count:
    print("Sentiment:", ("+" * happy_count) + ("-" * sad_count), "\nThis is a sad sentence.")
