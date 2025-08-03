# Note: List is mutable, not like string that is immutable 

super_heroes = ["Ironman", "Batman", "Superman", "Hulk"]
print(super_heroes)

super_heroes.append("Logan") # To add new value in the end
print(super_heroes)

print(super_heroes[4])  # To print a specific index value

print(super_heroes.pop(3)) # To remove a specific value by giving its index, You can also the print the removed value
print(super_heroes)

super_heroes.insert(3, "Deadpool")
print(super_heroes)

super_heroes.sort() # Sort the names alphabetically 
print(super_heroes) 

li = ["Butcher", 223, 192.09, "London", True] # A list can stores different data types values
print(li)

num = [14, 8, 22, 0, 36, 90, 61]

num.reverse() # reverse the list values
print(num)

num.remove(8)  # Remove the value
print(num)

num.sort() # sort the values
print(num)

