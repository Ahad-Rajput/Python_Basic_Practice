# Write a program to create a multiplication table of a number taking as an input from User, by using Loop.

num = int(input("Enter number : "))

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")