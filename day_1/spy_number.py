#spy number or not eg 1124
n = int(input("Enter a number "))
m = n
li = []
while n > 0:
    li.append(n%10)
    n = int(n/10)

total = 0
prod =1
for i in range(0, len(li)):
    total+=li[i]
    prod*=li[i]

if total == prod:
    print(f"{m} is a spy number")
else:
    print(f"{m} is not a spy number")

