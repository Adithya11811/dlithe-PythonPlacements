#to reverse a string

str1= "HEllo"
n =len(str1)
rstr = ""
for i in range(0, n):
    rstr+=str1[n-i-1]

print(rstr)