"""
Implement a function signFunc(x) that returns:

-> 1 if x is positive.
-> -1 if x is negative.
-> 0 if x is equal to 0.

You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product). 
"""

nums = [-1,-2,-3,-4,3,2,1]

def signFunc(nums):
    negative_count = 0

    for num in nums:
        if num == 0:
            print(0)
        elif num < 0:
            negative_count += 1
        
    if (negative_count % 2 == 1):
        print(-1)
    else:
        print(1) 
    
signFunc(nums)