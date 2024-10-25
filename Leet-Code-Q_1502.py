"""
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false
"""

arr = [-13,-17,-8,-10,-20,2,3,-19,2,-18,-5,7,-12,18,-17,12,-1]
# arr = [3,5,1]
sort = sorted(arr)
print(sort)

difference = sort[1] - sort[0]
is_arithmetic = True

for i in range(2, len(sort)):
    if ((sort[i] - sort[i-1]) != difference):
        is_arithmetic = False
        break

if is_arithmetic:
    print("True")
else:
    print("False")