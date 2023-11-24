"""
Title     : Write a Function
Subdomain : Introduction
Domain    : Python
Author    : Daniel Coutinho
Created   : 24 Nov 2023
Problem   : https://www.hackerrank.com/challenges/write-a-function/problem
"""

def is_leap(year):
    leap = False
    
    # Write your logic here
    
    x = year
    
    if (x % 4 == 0): #The year can be evenly divided by 4, is a leap year
        leap = True
        if (x % 100 == 0): #The year can be evenly divided by 100, it is NOT a leap year
            leap = False
            if (x % 400 == 0): #The year is also evenly divisible by 400. Then it is a leap year
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))
