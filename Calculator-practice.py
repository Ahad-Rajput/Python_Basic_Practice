#Fucntion to add two numbers
def add(a, b):
    return a + b
#Fucntion to subtract two numbers
def sub(a, b):
    return a - b
#Fucntion to multiply two numbers
def mult(a, b):
    return a * b
#Fucntion to divide two numbers
def div(a, b):
    if a == 0:
        print("Cannot divide by zero.")
    return a / b

while True:
    print("Options:")
    print("Enter 'add' for Addition")
    print("Enter 'subtract' for Subtraction")
    print("Enter 'multiply' for Multiplication")
    print("Enter 'divide' for Division")
    print("Enter 'quit' to end the program")

    user_input = input(">>>>> Enter your choice : ")
    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide"):
        num1 = int(input("Enter 1st num : "))
        num2 = int(input("Enter 2nd num : "))

    if user_input == "add":
        print(">>> Result : ", add(num1, num2))
    elif user_input == "subtract":
        print(">>> Result : ", sub(num1, num2))
    elif user_input == "multiply":
        print(">>> Result : ", mult(num1, num2))
    elif user_input == "divide":
        print(">>> Result : ", div(num1, num2))
    else:
        print("Invalid input....")