# Write a program to greet the names present in the list whose name start with 'S'

names = ["Ahad", "Amir", "Ans", "Irfan", "Muhammad", "Saif", "Sulaiman", "Zeeshan"]

for i in names:
    if(i.startswith("S")):
        print(f"Hello, {i}")
