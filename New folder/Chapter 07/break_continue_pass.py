i = 1

while(i<10):
    if(i == 7):
        break  # Instruct the program to exit from the loop
    print(i)
    i = i+1
print("-------------------------------------------")
for i in range(1, 10):
    if(i == 7):
        continue
    print(i)
print("-------------------------------------------")

for i in range(10):
    pass

print("<------------- End -------------->")