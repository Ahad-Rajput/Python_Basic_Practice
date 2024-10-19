"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
"""

word = "abab"
# Concatenate the string with itself
s = word + word

# Removes the first and last characters from the string s
ans = s[1:-1]

print(ans)
# Check if the original word is in the modified string
if word in ans:
    print(True)
else:
    print(False)