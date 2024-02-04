#1
if 5 > 2:
  print("Five is greater than two!")
#2
if 5 > 2:
 print("Five is greater than two!")  
if 5 > 2:
        print("Five is greater than two!") 
#3
x = 5
y = "Hello, World!"
#4
#This is a comment.
print("Hello, World!")

#comments

#This is a comment
print("Hello, World!")
#2
print("Hello, World!") #This is a comment
#3
#print("Hello, World!")
print("Cheers, Mate!")
#4
#This is a comment
#written in
#more than just one line
print("Hello, World!")
#5
"""
This is a comment
written in 
more than just one line
"""
print("Hello, World!")

#variables
#1
x = 5
y = "John"
print(x)
print(y)
#2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
#3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#4
x = 5
y = "John"
print(type(x))
print(type(y))
#5
x = "John"
# is the same as
x = 'John'
#6
a = 4
A = "Sally"
#A will not overwrite a
#7
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#8
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#9
x = y = z = "Orange"
print(x)
print(y)
print(z)
#10
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#11
x = "Python is awesome"
print(x)
#12
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#13
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#14
x = 5
y = 10
print(x + y)
#15
x = 5
y = "John"
print(x, y)
#16
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#17
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#18
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#19
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#data type

#1
x = 5
print(type(x))
#2
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))
x = None
x = memoryview(bytes(5))
x = bytearray(5)
x = frozenset({"apple", "banana", "cherry"})
x = {"apple", "banana", "cherry"}

#numbers
#1
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#2
print(type(x))
print(type(y))
print(type(z))
#3
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
#4
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
#5
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
#6
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
#7
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
#8
import random
print(random.randrange(1, 10))

#casting
#1
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
#2
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
#3
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

#strings
#1
print("Hello")
print('Hello')
#2
a = "Hello"
print(a)
#3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#4
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#5
a = "Hello, World!"
print(a[1])
#6
for x in "banana":
  print(x)
#7
a = "Hello, World!"
print(len(a))
#8
txt = "The best things in life are free!"
print("free" in txt)
#9
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#10
  txt = "The best things in life are free!"
print("expensive" not in txt)
#11
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
#12
b = "Hello, World!"
print(b[2:5])
#13
b = "Hello, World!"
print(b[:5])
#14
b = "Hello, World!"
print(b[2:])
#15
b = "Hello, World!"
print(b[-5:-2])
#16
a = "Hello, World!"
print(a.upper())
#17
a = "Hello, World!"
print(a.lower())
#18
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#19
a = "Hello, World!"
print(a.replace("H", "J"))
#20
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
#21
a = "Hello"
b = "World"
c = a + b
print(c)
#22
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#23
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#24
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#25
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#26
txt = "We are the so-called \"Vikings\" from the north."

