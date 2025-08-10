# Simple for loop

for i in range(1,11):
    print(i)

print("\n-------------------------------------------------\n")

# For loop with string

st = "Butcher"

for i in st:
    print(i)


print("\n-------------------------------------------------\n")


# For loop with list

names = ["Ahad", "Amir", "Ans", "Irfan", "Muhammad", "Saif", "Sulaiman", "Zeeshan"]

for i in names:
    print(i, end= ", ")

print("\n-------------------------------------------------\n")

# For loop with tuple

tup = (1, 3, 5, 7, 9, 11, 13, 15)
print("[", end=" ")
for i in tup:
    print(i, end=" ")
else:
    print("]")
