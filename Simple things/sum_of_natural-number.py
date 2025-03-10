limit = int(input("Enter the limit : "))

sum = 0

for i in range(1, limit + 1):
    sum += i

print(f"Sum of Natural numbers upto {limit} : {sum}")