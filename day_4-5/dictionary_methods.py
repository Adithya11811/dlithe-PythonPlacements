this_dict = {
    "brand":"Ford",
    "model":"mustang",
    "yr":1984
}

thisdict2 = dict(name="John", age=34, country="USA")
print(this_dict)


my_dict = {}

my_dict["name"] = "John"
my_dict["age"] = "23"
my_dict["year"] = 2001

print(len(my_dict))
print(type(my_dict))

print("Name: ", my_dict['name'])
x = my_dict.keys()
print(x)

y=my_dict.values()
print(y)

z=my_dict.items()
print(z)

c =my_dict.get("year")
print(c)

for x in my_dict:
    print(x)

for x in my_dict:
    print(my_dict[x])

print("Keys: ")
for x in my_dict.keys():
    print(x)

print("Values: ")
for x in my_dict.values():
    print(x)

print("Key-value pairs: ")
for key, value in my_dict.items():
    print(key,':',value )

if 'name' in my_dict:
    print("'name' exists in the dictionary")
else:
    print("'name' doesn't exist in the dictionary")

#modifications
my_dict['age'] = 24
print("Modified age: ", my_dict['age'])

my_dict.update({'age':45})
print("Modified age: ", my_dict['age'])

#adding to dictionary
my_dict['color1'] = 'green'
print(my_dict)

my_dict.update({'color2':'red'})
print(my_dict)

rmvd_value = my_dict.pop('year')
print(rmvd_value)
print(my_dict)

my_dict.popitem()
print(my_dict)

my_dict.clear()
print(my_dict)

del my_dict
# print(my_dict)


#nested dictionary
myfamily = {
    "child1":{
        'name':'Emil',
        'year':2004
    },
    "child2":{
        'name':'Tobias',
        'year':2007
    },
    "child3":{
        'name':'Linus',
        'year':2011
    }
}

for k,obj in myfamily.items():
    print(k)
    for nk in obj:
        print(nk, ' : ', obj[nk])

