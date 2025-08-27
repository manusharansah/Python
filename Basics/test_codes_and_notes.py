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

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)
# print(mytuple.count('apple'))
# print(mytuple.index('apple'))

# set = {True, 3}

# print(len(set))
# for x in set:
#     print(x)
# t1 = ('a','b','c')
# t2 = ('p','q','r')
# t3 = t1 + t2
# print(t3)
# print(type(t3))
# x = list(t2)
# x.extend(t1)
# print(x)


# s1 = {1,2,3}
# s2 ={True, False}
# s2.update(s1)
# print(s2)
# print(len(s2))
# s2.add("Habibi")
# print(s2)
# s2.remove('Habibi')
# s2.add("Mafia")
# s2.pop()  # removes a random value from the set
# s2.discard("Habibi")
# print(s2)

#Set Operations
# s1 = {1,2,3,4,5}
# s2 = {1,3,5,7,9}
# s3 = s1.union(s2) # s3 = s1 | s2
# s4 = s1 & s2 # intersection()
# s5 = s1 - s2 # difference()
# s6 = s1 ^ s2 # symmetric_difference()
# print(s1,s2,s3,s4,s5,s6)
# print(s1.isdisjoint(s2))

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# print(len(thisdict))

# dict1 = dict(name="manu", hobby ="Cricket", age = 21)
# print(dict1)
# print(dict1.get('name'))
# print(dict1.keys())

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()
# y = car.values()
# print(x) #before the change
# print(y)
# car["color"] = "white"

# print(x) #after the change
# print(y)
#This means that keys() method is a reference to a container and not an container
#Same is for values() methos as well
# print(car.items())
# Same for items() method as well
# car.update(color = "black")
# car.update({"color":"white"})
# new_dict = dict({"color": "white"})
# print(new_dict)
# print(type(new_dict))


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)
# thisdict.popitem() #removes a random item from the dictionary

# a = [1,4,5,7]
# del a[3]
# print(a)
# del a
# print(type({}))

# for x in thisdict:
#     print(x)

# new_dict = thisdict.copy()
# print(new_dict)
# print(type(new_dict))

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# for x, obj in myfamily.items():
#   print(x)

#   for y in obj:
#     print(y + ':', obj[y])

# car = {"brand": "Ford", "model": "Mustang"}

# print(car.setdefault("model", "abc"))   # Mustang (already exists)
# print(car.setdefault("year", 1964))         # Adds 'year': 1964

# print(car)
# # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


# def my_function(*kids):
#   print("The youngest child is " + kids[0])

# my_function("Emil", "Tobias", "Linus")

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def __str__(self):
#     return f"{self.name}({self.age})"
#   def abc(self):
#     print("Habibi ", self.name)

# p1 = Person("John", 36)
# p1.abc()
# print(p1.name)
# del p1.name
# try:
#     print(p1.name)
# except:
#   pass

# l = [1,2,3,4,5,6,7,8,9,0]
# abc = iter(l)
# while(atr:=(next(abc))):
#     print(atr)

# class Habibi():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a
#         self.a+=1
#         if x<=20:
#             return x
#         else:
#             raise StopIteration

# per = iter(Habibi("Manu","21"))
# for x in per:
#     print(x)

# class Car():
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Drive")
# class Ship():
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Sail")
# class Bike():
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("BhuTuTuTu")

# x = Car("BMW","M4")
# y = Ship("Artesania Latina",'HMS Victory')
# z = Bike("Yamaha",'Supersport')

# for obj in (x,y,z):
#     obj.move()

# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Move!")

# class Car(Vehicle):
#   pass

# class Boat(Vehicle):
#   def move(self):
#     print("Sail!")

# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()
# x = 20
# y = 4
# def abc():
#     y = 20
#     print(y)
#     def xyz():
#         nonlocal y
#         y = 30
#     print(y)
#     xyz()
#     print(y)
# abc()

# import platform
# x = platform.system()
# print(x)

# x= dir(platform)
# print(type(x))
# print(x)

# import datetime

# x = datetime.datetime.now()

# print(x.year)
# print(x.strftime("%a"))
# today = datetime.datetime(2025,8,24)
# print(today.strftime("%a"))


# import json
# l= [1.4,"Habibi"]
# x = json.dumps(l, indent = 4)
# print(type(x))
# print(x)
# print(json.dumps(l, indent=4, separators=(". ", " = ")))
# y = json.loads(x)
# print(type(y))
# print(y)
# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x,indent=4)

# # the result is a JSON string:
# print(y)


# import camelcase
# y = camelcase.CamelCase().hump("Hey Habibi. Come to Dubai")
# print(y)
# c = camelcase.CamelCase()

# txt = "hello world"

# print(c.hump(txt))

# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")


# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

# x = "hello"

# if not type(x) is int:
#   raise TypeError("Only integers are allowed")

# x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

# x = input("Ebter your age: ")
# print(y)


# import math
# y = True
# while y:
#     try:
#         x = int(input("Enter a number: "))
#         y = False
#     except:
#         print("Wrong input!")

# print(f"The square root is {math.sqrt(x)}")

# import cowsay
# cowsay.cow("Good Morning")

# File Handling In Python
"""
To read the contents of a file we use the function read()
for example we use f.read(). 
Also to get line by line content of the file we use the for loop as:
for x in f:
    print(x)
"""
fname = "shakira-shakira.txt"
# with open(fname,'w+') as f:
#     str = "Shake Up your body just like me."
#     f.write(str)


# import os
# try:
#     os.remove(fname)
# except:
#     print(f"File {fname} doesn't exist.")

