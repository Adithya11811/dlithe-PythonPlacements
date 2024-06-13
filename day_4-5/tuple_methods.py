my_tuple = (1,2,3)
another_tuple = tuple([4,5,6])

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:3])
print()
combined_tuple = my_tuple + another_tuple
print(combined_tuple)
print()
repeated_tuple = my_tuple *3
print(repeated_tuple)
print()
print(2 in my_tuple)

print(4 not in my_tuple)
print(len(my_tuple))
print()
for i in my_tuple:
    print(i)
print()

str_to_tuple = tuple("hello")
print(str_to_tuple)
list_to_tuple = tuple([4,5,6])
print(list_to_tuple)
print(my_tuple.count(2))
print(my_tuple.index(3))

tuple_of_int = (5,2,4,5,1,9)
sort_tuple = tuple(sorted(tuple_of_int))
print("Sorted Tuple: ", sort_tuple)

t_of_t= ((1, 'apple'), (2, 'orange'), (3,'cherry'), (4,'banana'))
sorted_t = sorted(t_of_t, key= lambda x:x[1])
print(sorted_t)

s = tuple(x**2 for x in range(1,6))
print(s)

l1 = [1,2,3]
l2 = ['apple', 'banana', 'cherry']
z =tuple(zip(l1,l2))
print(z)


