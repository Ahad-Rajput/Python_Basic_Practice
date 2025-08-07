dict = {
    "name" : "Ahad",
    "age" : 20,
    "list" : [10, "Butcher", True],
    0 : "Hello", 
    "Programmer" : True
}

print(dict.items()) #To print all the itmes(keys & values) present in the dictionary
print(dict.keys()) # To print only keys present in the dictionary
print(dict.values()) # To print only values present in the dictionary

print(dict["Programmer"]) # To get a specific value of a key, If the key is not present in the dictionary "Gives Error"
print(dict.get("Programmer")) # To get a specific value of a key 
print(dict.get("Python")) # If the key is not present in the dictionary prints "None"
print(dict.get("Python", "Not Found")) # If the key is not present in the dictionary prints "Not Found"

dict.update({0 : "Hey"})  # Update the values..
dict.update({"Language" : "Python & C++"})  # If the key is not present in the dictionary, It creates the key and assign it the value
print(dict)

item = dict.popitem() # Remove an item from the dictionary by using the LIFO(Last In First Out) rule
print(item)

print(dict)

itme1 = dict.pop("list") # Remove a specific item from the dictionary
print(itme1)

print(dict)