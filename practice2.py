def binary_search(list, target):
    found = False
    start = 0
    end = len(list) + 1 
    mid = int((start + end) / 2)
    for i in list:
        if target == list[mid]:
            found = True
            print(f"{target} is found.")
            break
        elif target > list[mid]:
            start = mid + 1
        elif target < list[mid]:
            end = mid - 1
        mid = int((start + end) / 2)
    if found != True:
        print(f"{target} is not found.")

num = int(input("Enter the number, You want to find : "))

list = [1,2,3,4,5,6,7,8,9]

binary_search(list, num)