def create_tuple():
    tuple1 = (1,2,3,4,5)
    tuple2 = ('a','b','c','d', 'e')
    tuple3 = ('apple', 'banana', 'cherry')
    return tuple1, tuple2, tuple3

tuple1, tuple2, tuple3 = create_tuple()

def access_tuple_items(tuple1, tuple2):
    print("Tuple 1:", tuple1)
    print("FIrst element of tuple 1: ", tuple1[0])
    print("Last element of tuple 1: ", tuple1[-1])
    print("Tuple 2:", tuple2)
    print("Second element of tuple 2: ", tuple2[1])
    print("Second Last element of tuple 2: ", tuple2[-2])
    print(tuple1[0:5])

access_tuple_items(tuple1, tuple2)

def unpacking_tuple(tuple3):
    (green, yellow, red) = tuple3
    print(green)
    print(yellow)
    print(red)

unpacking_tuple(tuple3)

def unpacking_tuple2():
    fruits = ("apple", "banana", "cherry", "strawbwerry", "raspberry")
    (green, yellow, *red) = fruits
    print(green)
    print(yellow)
    print(red)

unpacking_tuple2()

def changeTuples(tuple1, tuple2):
    list1 = list(tuple1)
    list2 = list(tuple2)
    list1.append(6)
    list2.remove('a')
    tuple1 = tuple(list1)
    tuple2 = tuple(list2)
    return tuple1, tuple2

def loop_through_var(tuple1):
    print("Looping through tuple 1 using for loop:")
    for item in tuple1:
        print(item)

    print("\n Looping using while loop and index")
    i = 0
    while i < len(tuple1):
        print(tuple1[i])
        i+=1

def join_tuples(tuple1, tuple2):
    tuple3 = tuple1+tuple2
    return tuple3


tuple1, tuple2 = changeTuples(tuple1, tuple2 )

print("After changes")
access_tuple_items(tuple1, tuple2 )
print()

tuple3  = join_tuples(tuple1, tuple2)
print("Joined Tuple:", tuple3)





