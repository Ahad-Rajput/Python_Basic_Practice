# Write a program to take a number as input from User and check if it prime or not..


num = int(input("Enter number: "))

for i in range(2, num):
    if((num%i) == 0):
        print("Number is not prime.")
        break
else:
    print("This is a prime number.")