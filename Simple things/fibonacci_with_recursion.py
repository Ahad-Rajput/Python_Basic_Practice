def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
    
nTerms = int(input("Enter the number of terms : "))

if(nTerms <= 0):
    print("Enter +ve number.")
else:
    print("Fibonacci Sequence : ")
    for i in range(nTerms):
        print(recur_fibo(i))
        