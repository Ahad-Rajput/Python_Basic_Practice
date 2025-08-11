# Fahrenheit to Celsius

def f_to_c(temp):
    return 5*(temp-32)/9

fahrenheit = int(input("Enter temperature in Fahrenheit: "))

celsius = f_to_c(fahrenheit)

print(f"{round(celsius, 2)}°C")