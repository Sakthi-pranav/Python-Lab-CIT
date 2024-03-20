def fibo(x):
    if x == 1:
        return 0
    if x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)
        
n  = int(input("Enter a number : "))
i = 1
while i<=n:
    ans = fibo(i)
    print(ans)
    i+=1 
