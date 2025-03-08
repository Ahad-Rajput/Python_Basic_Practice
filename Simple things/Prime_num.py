num = int(input("Enter a number : "))

#define a flag variable -> False, to show num is prime
flag = False

if num == 1:
    print(f"{num}, is not a prime number")
elif num > 1:
    for i in range(2, num):
        if(num % i) == 0:
            flag = True  #if found , set flag -> True, to show num is not prime
            break # break out of loop

if(flag == True):
    print(f"{num} is not a prime number.")
else:
    print(f"{num} is a prime number.")