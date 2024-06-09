#strong number or not eg: 145
#the sum of factorial of individual digits is equal to the number itself


n = int(input("Enter a number "))
m = n
li = []

def factorial(n):
    if n==0 or n ==1:
        return 1
    return n * factorial(n-1)

while n > 0:
    li.append(n%10)
    n = int(n/10)

total = 0
for i in range(0, len(li)):
    total += factorial(li[i])

if total == m:
    print("Given number is a strong number")
else:
    print("Not a strong number")

