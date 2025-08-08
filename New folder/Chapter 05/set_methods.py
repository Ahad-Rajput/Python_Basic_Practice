s1 = {10, 21, 90, 1, "Butcher", 0}
s2 = {"Butcher", 100, 12, 9, 1, 7}

print(s1.union(s2))  # Prints the union of two sets
print(s1.intersection(s2))  # Prints the Intersection of two sets


s = {6, 71, 23, 30, 41, 23, 0, 23}
print(f"Orignial set : {s}")  # Set doesn't contain duplicate values
print(type(s))

s.add(300) # To add a new value in the set
print(f"Updated set : {s}")

s.remove(6) # To remove a specific value from the set
print(f"Updated set : {s}")

s.pop() # To remove a random value from the set
print(f"Updated set : {s}")

s.clear() # Clear all the data from the set and make it empty
print(f"Updated set : {s}")