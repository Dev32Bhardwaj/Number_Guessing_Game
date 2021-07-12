# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 23:24:09 2021

@author: usetr2
"""
import random
#sudoko solver, Number Guessing, converter
def guess(n):
    score=0
    while True:
        i=int(input("enter your guess "))
        if i not in range(1,11):
            print("invalid number")
        elif i==n:
            print("correct guess")
            score+=10
            break
        elif i%n==0:
            print(i,"is a multiple of given value")
        elif n%i==0:
            print(i,"is a factor of given value")
        elif i>n:
            print(i,"is greater than the given value")
        elif i<n:
            print(i,"is smaller than the given value")
        score-=1
    return score
n=random.randint(1,10)
print(n)
print(guess(n))
        