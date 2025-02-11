def linear_Search(list, target):
    found = False
    for i in list:
        if target == i:
            found = True
            print(f"{target} is in the list")
            break
    if found != True:
        print(f"{target} is not in the list")


num = int(input("Enter the number, You want to find : "))

list = [89, 5,3,34,90]
linear_Search(list, num)
