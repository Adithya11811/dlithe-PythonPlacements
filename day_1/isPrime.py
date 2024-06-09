#write a program to check if a number is a prime or not
n = int(input("Enter a number"))

def isPrime(n):
    if n == 1:
        return False
    if n==2 or n == 3:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if isPrime(n):
    print(f"The number {n} is a prime number")
else:
    print(f"The number {n} is not a prime number")
