# neon number or not, eg: 9

n = int(input("Enter a number "))
m = n
li = []
n = n*n
while n > 0:
    li.append(n%10)
    n = int(n/10)

total = 0
for i in range(0, len(li)):
    total+=li[i]

if total == m:
    print(f"{m} is a neon number")
else:
    print(f"{m} is not a neon number")

