"""
Given two strings s and t, return true if t is an 
anagram of s, and false otherwise.
"""
s = 'anagram'
t = 'nagaram'

def isAnagram(s,t):
    # Check if the lengths are equal
    if(len(s) != len(t)):
        return False
        
    # Sort both strings and compare
    return sorted(s) == sorted(t)


if(isAnagram(s,t) == True):
    print(f"'{t}' is anagram of '{s}'.")
else:
    print(f"'{t}' is not anagram of '{s}'.")