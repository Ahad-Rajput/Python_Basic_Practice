"""
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false
"""

arr = [-13,-17,-8,-10,-20,2,3,-19,2,-18,-5,7,-12,18,-17,12,-1]
sort = sorted(arr)
print(sort)
i = 0
if (sort[i]-sort[i+1]) == (sort[i+1]-sort[i+2]):
    print("True")
else:
    print("False")
