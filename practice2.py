def binary_search(arr, target):
    
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = int(start+end / 2 )

        if target == arr[mid]:
            print(f"{target} is present at {mid} index.")
            return
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1 
    print(f"{target} is not present in array.")



arr = [2, 4, 6, 8, 10, 12, 14, 16]

num = int(input("Enter number, you want to find : ")) 

binary_search(arr, num)