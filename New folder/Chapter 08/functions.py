# Definition of function
def greet(name, ending="Thank you😊"):
    print(f"Good Day, {name}")
    print(ending)


greet("Ahad")  # Function call
greet("Saif", "Thanks🙂")


def add(num1, num2):
    return num1 + num2

n1 = int(input("Enter num1: "))
n2 = int(input("Enter numb2: "))

result = add(n1, n2)
print(f"Result: {result}")

