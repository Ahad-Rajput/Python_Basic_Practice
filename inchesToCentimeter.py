def inchesToCentimeter(inches):
    if(inches < 0):
        print("The given measurement must be non-negative.")
    else:
        print(f"{inches} inches = {2.54*inches} centimeter")
    
var = float(input("Enter inches: "))
inchesToCentimeter(var)
