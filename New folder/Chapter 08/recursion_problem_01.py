'''
sum(n) = 1 + 2 + 3 + ... + n
'''

def sum(n):
    if(n == 1):
        return 1
    return n + sum(n-1)

num = int(input("Enter number: "))

result = sum(num)

print(f"Result: {result}")