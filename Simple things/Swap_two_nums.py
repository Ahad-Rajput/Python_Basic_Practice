#Input two numbers
num1 = input("Enter num1 : ")
num2 = input("Enter num2 : ")
print(f"Original values : num1 = {num1} , num2 = {num2}")
#Swaping the values using temporary variable
temp = num2
num2 = num1
num1 = temp
print(f"Swapped values : num1 = {num1} , num2 = {num2}")