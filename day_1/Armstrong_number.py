
#armstrong number or not eg: 371

n = int(input("Enter a number "))
m = n
li = []

def poweroflenofnum(n,m):
    return n ** len(str(m))

while n > 0:
    li.append(n%10)
    n = int(n/10)

total = 0
for i in range(0, len(li)):
    total += poweroflenofnum(li[i], m)

if total == m:
    print("Given number is a Armstrong number")
else:
    print("Not a Armstrong number")
