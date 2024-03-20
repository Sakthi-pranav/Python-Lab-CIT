n = int(input("Enter a number : "))
is_prime = True
for i in range(2,n):
    if n % i == 0:
       is_prime = False
print("Prime") if is_prime == True else print("Composite")
