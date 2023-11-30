"""
Title     : Find the Runner-Up Score!
Subdomain : Basic Data Types
Domain    : Python
Author    : Daniel Coutinho
Created   : 30 Nov 2023
Problem   : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr_alt = list(set(arr)) #converting the input list to a set
    arr_alt.sort()
    print(arr_alt[-2]) #prints the second to last item 
