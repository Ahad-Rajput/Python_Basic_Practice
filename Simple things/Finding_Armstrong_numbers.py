# Input the interval from the user
lower = int(input("Enter the lower limit of the interval : "))
upper = int(input("Enter the upper limit of the interval : "))

for num in range(lower, upper + 1):
    num_digits = len(str(num))
    temp_num = num
    sum = 0
    
    while temp_num > 0:
        digit = temp_num % 10
        sum += digit ** num_digits
        temp_num //= 10

    if sum == num:
        print(num)