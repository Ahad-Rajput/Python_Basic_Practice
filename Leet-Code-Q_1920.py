""""
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
"""

nums = [5,3,1,0,2,4]

# Create an empty list with name 'ans' size as nums
ans = [0]*len(nums)

# Fill 'ans' according to the problem's requirement
for i in range(len(nums)):
    ans[i] = nums[nums[i]]

print(ans) 