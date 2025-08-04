# Write a program to enter marks of Programming Fundamental of 6 Students and print the data in sorted form

marks = []
m1 = int(input("Enter your makrs : "))
marks.append(m1)
m2 = int(input("Enter your makrs : "))
marks.append(m2)
m3 = int(input("Enter your makrs : "))
marks.append(m3)
m4 = int(input("Enter your makrs : "))
marks.append(m4)
m5 = int(input("Enter your makrs : "))
marks.append(m5)
m6 = int(input("Enter your makrs : "))
marks.append(m6)

marks.sort()
print(marks)