#factorial of given number
n = int(input("Enter a number "))

def factorial(n):
    if n==0 or n ==1:
        return 1
    return n * factorial(n-1)

print(f"Factorial of {n} is {factorial(n)}")
