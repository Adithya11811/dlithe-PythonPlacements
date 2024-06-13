from collections import namedtuple
import math

Point = namedtuple('Point', ['x', 'y'])

point1 = Point(1,2)
point2 = Point(4,6)

d = math.sqrt((point2.x-point1.x) ** 2 + (point2.y - point2.y) ** 2)
print(f"distance between point1-{point1} and point2-{point2}: ", d)

#filter and reduce

t1 = (1,2,3,4,5,6)
filetered_t = tuple(filter(lambda x: x%2 == 0, t1))
print(filetered_t)


from functools import reduce

def add(x,y):
    return x+y

res = reduce(add, t1)
print(res)