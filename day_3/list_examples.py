l1 = ["apple", "banana", "cherry", "mango"]
l2 = [10, 20, 30, 40]
l3 = [True, False]
l4 = list(("Jack"))
l5 = list(("Jack","John"))

print(l4)
print(l5)
print(l1[0])
print(l1[0:4])
print(l1[:4])
print(l1[:])
print(l1[0:])
print(l1[-4:-1])

print(l1[-1:-4])
print(len(l1))
print(type(l1))
print(type(l1[0]))
if "apple" in l1:
    print("Exists")

l1[1] = "Kiwi"
print(l1)
l1[1:3] = ["pineapple", "Dates","x"]
print(l1)

list = ["apple", "banana", "cherry"]
list[1:2] = ["blackcurrent", "watermelon"]
print(list)

list = ["apple", "banana", "cherry"]
list[1:3] = ["watermelon"]
print(list)

list.insert(1, "obj")
print(list)

list.append("obj2")
print(list)

list1 = ["apple", "banana", "cherry"]
list2 = ["mango", "pineapplee", "papaya"]
list1.extend(list2)
print(list1)

list1 = ["apple", "banana", "cherry", "banana"]
list1.remove("banana")
print(list1)


thislst = ["apple", "banana", "cherry"]
i = 0
while i < len(thislst):
    print(thislst[i])
    i +=1

#list comprehensions
[print(x) for x in thislst]

#method 1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
nl = []
for x in fruits:
    if 'a' in x:
        nl.append(x)

print(nl)

#method-2
nl = [x for x in fruits if 'a' in x]
print(nl)

thislst = [100, 30, 58, 67, 2]
thislst.sort()
print(thislst)

thislst = [100, 30, 58, 67, 2]
thislst.sort(reverse=True)
print(thislst)

#sort the number on how close it is to 50
#customized sort
def fun(n):
    return abs(n-50)

thislst = [100, 52, 58, 73, 85, 31]
thislst.sort(key=fun)


print(thislst)

thislst = ['apple', 'Apple', 'grapes', 'banana']
thislst.sort(key=str.lower)
# thislst.sort()
print(thislst)

def swap(li, p1, p2):
    temp = li[p1]
    li[p1] = li[p2]
    li[p2] = temp
    return li

thislst = [100, 52, 58, 73, 85,2, 32]
swap(thislst, 2 ,3)
print(thislst)

sum = 0
for x in thislst:
    sum+=x

print(sum)
 
print(thislst[0])
print(thislst[len(thislst)-1])

mini = thislst[0]
maxi = thislst[0]

for i in thislst:
    if i > maxi:
        maxi = i
    elif i <mini:
        mini = i

print(mini)
print(maxi)