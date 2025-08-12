# Snake-Water-Gun Game

import random  # Library to generate random values

options = '''
s for Snake
w for Water
g for Gun
'''
print(options)
choice = input("Enter your choice (s/w/g): ")  # Taking input from user

comp = random.choice(['s', 'w', 'g'])  # Generate a random number from (s, w, g)

dict = {'s' : 1, 'w' : -1, 'g' : 0}  # dictionary that take int value of char
reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"} # dictionary to show what we choose

human = dict[choice]  # store int value of user choice in 'human' variable
computer = dict[comp]  # store int value of computer choice in 'computer' variable

print(f"You chose: {reverseDict[human]}\nComputer chose: {reverseDict[computer]}")

# Logic Portion

if(computer == human):
    print("This is draw!")
else:
    if(computer == -1 and human == 1):
        print("You win!")
    elif(computer == -1 and human == 0):
        print("You lose!")
    elif(computer == 1 and human == -1):
        print("You lose!")
    elif(computer == 1 and human == 0):
        print("You win!")
    elif(computer == 0 and human == -1):
        print("You win!")
    elif(computer == 0 and human == 1):
        print("You lose!")
    else:
        print("Something went wrong!")