def isPrime(n):
    is_prime = True
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
    return is_prime
    
n = int(input("Enter a number :"))
for i in range(1, n+1):
    if isPrime(i) == True:
        print(i)
        
