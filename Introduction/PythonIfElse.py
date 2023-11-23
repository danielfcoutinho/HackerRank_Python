"""
Title     : Python If-Else
Subdomain : Introduction
Domain    : Python
Author    : Daniel Coutinho
Created   : 23 Nov 2023
Problem   : https://www.hackerrank.com/challenges/py-if-else/problem
"""

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

if (n % 2) != 0:
    print('Weird')
    
else:
    if (2 <= n <= 5):
        print('Not Weird')
    elif (6 <= n <= 20):
        print('Weird')
    else:
        print('Not Weird')
