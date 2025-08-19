#Dynamic Variables
'''
x = 5
print(x)
x = "Manu"
print(x)
'''

'''
x = int(4)
print(x)
x = 'GPA'
print(x)
'''

#Some Sentence Cases
#Pascal Case -> ManuSharanKumar
#Snake Case -> Manu_Sharan_Kumar
#Camel Case -> manuSharanKumar


# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)


# x = 4
# print(x)
# def myfunc():
#     global x
#     x = 3
#     print(3)
# myfunc()    

# x = 3 + 3j
# print(x)
# x = b"5"
# print(x)
# x = bytearray(5)
# print(x)
# x = memoryview(bytes(5))
# print(x)

# x = list(("apple", "banana", "cherry"))
# print(x)

# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# #convert from int to float:
# a = float(x)

# #convert from float to int:
# b = int(y)

# #convert from int to complex:
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))


# print(4 + 5j)

# import random
# print(random)

# print(complex(random.randint(3,10),random.random()))

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

# b = "Hello, World!"
# print(b[-5:-2])

# a = "Hello, World!"
# x = a.split(",")
# print(x)
# def sq(x):
#     return x**2

# print(f"I have NPRs.{sq(30):.2f}")

# print('I love You'.count("I"))
# class myclass():
#   def __len__(self):
#     return 0

# myobj = myclass()
# print(bool(myobj))
# print(isinstance(myobj,object))

# l = [1,3,5]
# even = [2,4,6]
# l.extend(even)
# print(l)

# r = range(9)
# print(3.1 in r)
# a = 5
# b =6
# d1 = int(a,2)
# d2 = int(b,2)
# c = a + b
# print(bin(c)[2:])


"Beginning of Day3"
#List Comprehensions

'Used for creating a list from a list without using loop and conditional separately'
"In list comprehension, any iterable like tuples, dictionary,etc can be used."

# x = [x**2 for x in range(100)]
# print(x)
# def myfunc(n):
#     return n  % 3
# x = [100,200,14,78]
# x.sort(key = myfunc,reverse=True)
# print(x)

# l = ['apple',"Mango","HaBIbi"]
# l = [x.lower() for x in l]
# print(l)


# a = 5
# b = a
# a = 4
# print(b)

# l = [1, 5, 7, 3, 9, 0]
# num = l[:]
# l[0] = 4
# print(l,num)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

# list1 = list1 + list2
# tu = tuple(list1)
# print(list1)
# print(list2)
# print(tu,type(tu))
# x,y,z = tuple(list1)
# print(x,type(x))

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
print(mytuple.count('apple'))
print(mytuple.index('apple'))