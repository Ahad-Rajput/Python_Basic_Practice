#Input both numbers
num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

print(f"Before Swapping : num1 = {num1} , num2 = {num2}")

#Swapping without using a temporary variable
num1 , num2 = num2 , num1

print(f"After Swapping : num1 = {num1} , num2 = {num2}")
