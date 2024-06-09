# generate all prime no's from 1 to n
n1 = int(input("Enter a range of numbers"))
n2 = int(input())

def isPrime(n):
    if n == 1:
        return False
    if n==2 or n == 3:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

li = []
def GenPrime(n1, n2):
    for i in range(n1,n2):

        if isPrime(i):
            li.append(i)

GenPrime(n1,n2)
print(li)