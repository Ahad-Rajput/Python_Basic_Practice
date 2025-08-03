# Note: Strings are immutable means you can't change the orignal string by applying functions, The result you get is the copy of the orignal string

str = "Batman"

print(str.endswith("man")) # Gives the Boolean value (T\F) if the string ends with that..

print(str.startswith("Ba")) # Gives the Boolean value (T\F) if the string starts with that..

print(str.startswith("ba")) # Prints False cuz 'B' & 'b' are not same


str2 = "pakistan"

print(str2.capitalize()) # Prints the string with first letter captial

print(str2.upper()) # Prints the string in upper case

print(str2.lower()) # Prints the string in lower case

print(len(str2))  # Gives the length of the string 

print(str2.isalpha()) # Gives true if the string contains alphabets 
# (Note: If you use spaces in the string it'll give you False cuz space isn't an alphabet)

name = "python course"

print(name.title())  # Prints the string in the form of title
print(name.find("course")) # Gives the index of the first letter  
print(name.count("o"))  # Gives the total no. of letter 'o' repeats

number = "1234"
print(number.isdigit()) # Gives true if the string contains digits
print(number.isdecimal()) # Gives true if the string contains decimals(0-9)

message = "I'm good."
print(message)

replace_str = message.replace("good", "fine")  # Replace the old_word with new_word
print(replace_str)