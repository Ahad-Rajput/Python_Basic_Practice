# Note: Like strings Tuples are also immutable

tup = (0, 25, 14, 63, 87, 9, 45, 0, 3)
no = tup.count(0) # Count the specific value
print(no)


tup1 = (1,) # To make a tuple that contains only one value, not like this -> tup1 = (1) 
print(type(tup1))


tup2 = (123, 76.0, True, "Butcher") # Also can store the different data type values
ind = tup2.index("Butcher") # Gives the index of the value you want to find
print(ind)
print(123 in tup2) # use 'in' to give (T\F) if that value is in the tuple
print("Homelander" in tup2)

num1 = (1, 2)
num2 = (3, 4)

num3 = num1 + num2  # Concatenation of two tuples
print(num3)

num = (2, 4)
multi_num = num * 3  # Increase the tuple values

print(multi_num)

a, b = num # Unpacked the tuple
print(a, b)