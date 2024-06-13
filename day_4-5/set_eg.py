s = {"apple","banana", "cherry"}
s.add("orange")
print(s)

s = {"apple","banana", "cherry"}
trop = {"pineapple","mango","papaya"}

s.update(trop)
print(s)

s.remove("banana")
print(s)

s.discard("grapes")
print(s)

s.pop()
print(s)

s.clear()
print(s)

del s
# print(s) #throws out error as s is completely deleted

s1 = {1,2,3,4,5}
s2 = {4,5,6,2,1}

s3 = s1.union(s2)
print(s3)

s3 = s1.intersection(s2)
print(s3)

s3 = s1.difference(s2)
print(s3)

s3 = s1.symmetric_difference(s2)
print(s3)

s1.intersection_update(s2)
print(s1)

s1 = {1,2,3,4,5}
s2 = {4,5,6,2,1}

s2.difference_update(s1)
print(s2)

s1 = {1,2,3,4,5}
s2 = {4,5,6,2,1}

s2.symmetric_difference_update(s1)
print(s2)