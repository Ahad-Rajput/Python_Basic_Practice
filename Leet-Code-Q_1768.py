"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string   
"""

word1 = "abcd"
word2 = "pqrstv"

ans = ""

i = 0
j = 0

A = len(word1)
B = len(word2)

# Merge characters in alternating order
while((i < A) and (j < B)):
    ans+=word1[i]
    ans+=word2[j]
    i += 1
    j += 1

# Append remaining characters from word1 (if any)
while(i < A):
    ans+=word1[i]
    i += 1

# Append remaining characters from word2 (if any)
while(j < B):
    ans+=word2[j]
    j += 1

print(ans)