# palindrome or not

pal = input("Enter a string ")
n = len(pal)-1
flag = True
nstr = pal
pal = pal.lower()

for i in range(0, len(pal)):
    if pal[i] != pal[n-i]:
        flag = False
        break

if flag:
    print(f"{nstr} is a palindrome")
else:
    print(f"{nstr} is not a palindrome")