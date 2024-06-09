#happy number or not, eg: 19
n = int(input("Enter a number "))
m = n

def sumofSquares(n):
    li = []
    while n > 0:
        li.append(n%10)
        n = int(n/10)

    total = 0
    for i in range(0, len(li)):
        total+=(li[i]*li[i])

    return total

while int(n/10) != 0:
    n = sumofSquares(n)

if n == 1:
    print(f"{m} is a happy number")
else:
    print(f"{m} is not a happy number")

