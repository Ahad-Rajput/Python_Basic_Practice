"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space
"""

arr = []
nums = [2,1,4,2,1]
# for num in nums:
#     if num not in arr:
#         arr.append(num)
#     else:
#         arr.remove(num)
# print(arr.pop())


result = 0
for num in nums:
    result ^= num
print(result)