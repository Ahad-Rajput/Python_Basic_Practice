'''
***
**  for n = 3
*
'''

def pattern(n):
    if(n == 0):
        return 
    print("*" * n)
    return pattern(n-1)

num = int(input("Enter number of lines of pattern: "))

pattern(num)