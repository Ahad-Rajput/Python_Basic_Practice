"""
Implement a function signFunc(x) that returns:

-> 1 if x is positive.
-> -1 if x is negative.
-> 0 if x is equal to 0.

You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product). 
"""

nums = [-1,-2,3,-4,3,2,1]

def signFunc(x):
    for i in range(len(nums)):
        x = x*nums[i]

    if x > 0:
        print("1")
    elif x < 0:
        print("-1")
    else:
        print("0")

signFunc(1)