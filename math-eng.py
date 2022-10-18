"""this doc is my python workplace for my math eng oop course"""

"""1-Hello World"""
"""To print a string in python3"""
#hello =("hello world")
#print(hello)

"""Variables and Types"""

"""1-Numbers"""
"""Python supports two types of numbers - integers(whole numbers) and floating point numbers(decimals). 
To define an integer, use the following syntax:"""
#myint = 7
#print(myint)

#myfloat = 7.0
#print(myfloat)

#myfloat = float(7)
#print(myfloat)

"""2-Strings"""
"""Strings are defined either with a single quote or a double quotes."""
#mystring = "hello"
#print(mystring)

#mystring = 'hello'
#print(mystring)

#one = 1
#two = 2
#three = one + two
#print(three)#

#hello = 'hello'
#world = 'world'

#helloworld = hello + " " + world 
#print(helloworld)

#a,b = 3,4
#print(a,b)

"""Exercise"""

#mystring = "hello"
#myfloat = 10.0
#myint = 20

#if mystring == "hello":
#    print("String: %s" % mystring)
#if isinstance(myfloat, float) and myfloat == 10.0:
#    print("Float: %f" % myfloat)
#if isinstance(myint, int) and myint == 20:
#    print("Integer: %d" % myint)



"""Lists"""

""" Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish. 
Lists can also be iterated over in a very simple manner. Here is an example of how to build a list.
 """
#mylist = []
#mylist.append(1)
#mylist.append(2)
#mylist.append(3)
#mylist.append(4)

#print(mylist[0])
#print(mylist[1])
#print(mylist[2])

#for x in mylist:
#    print(mylist)

"""Exercise"""

#numbers = []
#strings = []
#names = ["John", "Eric", "Jessica"]

#second_name = [names[1]]

#numbers.append(1)
#numbers.append(2)
#numbers.append(3)

#strings.append('hello')
#strings.append('world')

#print(numbers)
#print(strings)
#print("The second name on the names list is %s" % second_name)

"""Basic Operators"""
"""1-Arithmetic Operators"""
"""Just as any other programming languages, the addition, subtraction, multiplication, and division operators can be used with numbers.
"""
#number = 1 + 2 * 3 / 4.0
#print(number)

"""Another operator available is the modulo (%) operator, which returns the integer remainder of the division. dividend % divisor = remainder."""

#remainder = 11%3 
#print(remainder)

"""Using two multiplication symbols makes a power relationship."""
#squared = 5 ** 2
#cubed = 2 ** 3
#print(squared)
#print(cubed)

"""Using operators with Strings"""
"""Python supports concatenating strings using the addition operator:

"""

#helloworld= "hello" + " " + "world"
#print(helloworld)

#lotsofhello = "hello" * 10
#print(lotsofhello)

"""Using operators with lists"""
#even_numbers = [0,2,4,6,8]
#odd_numbers = [1,3,5,7,9]
#all_numbers = even_numbers + odd_numbers
#print(all_numbers)

#print([1,2,3] * 3)

"""Exercise"""

#x = object()
#y = object()


#x_list = [x] * 10
#y_list = [y] * 10
#big_list = x_list + y_list

#print("x_list contains %d objects" % len(x_list))
#print("y_list contains %d objects" % len(y_list))
#print("big_list contains %d objects" % len(big_list))


"""String Formatting"""

""" Python uses C-style string formatting to create new, formatted strings. 
The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), 
together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d". """


#name = "john"
#print("hello, %s" % name)

#name = "john"
#age = 21
#print("%s is %d years old." %(name,age))

""" 
%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)
"""

"""Exercise"""

#data = ("John", "Doe", 53.44)
#format_string = "Hello"

#print("Hello %s %s, Your current balance is  $%f." %(data[0], data[1], data[2]))

#data = ("John", "Doe", 53.44)
#format_string = "Hello %s %s. Your current balance is $%s."

#print(format_string % data)

"""Conditions"""
#x = 2
#print(x == 2)
#print(x == 3)
#print(x < 3)

"""Boolean Operators"""
"""The "and" and "or" boolean operators allow building complex boolean expressions"""
#name = "John"
#age = 23

#if name == "John" and age == 23:
#    print("Your name is John, and you are 23 years old.")

#if name == "John" or name == "Rick":
#    print("Your name is either John or Rick.")
"""The "in" operator could be used to check if a specified object exists within an iterable object container, such as a list:"""

#name = "John"

#if name in ["John", "Rick"]:
#    print("Your name is either John or Rick.")

"""Loops"""
"""The 'for' Loop"""
"""for loops iterate over a given sequence."""

#primes = [2,3,5,7]
#for x in primes:
#    print(x)

#for x in range(7):
#    print(x)


"""For loops can iterate over a sequence of numbers using the "range" and "xrange" functions. 
The difference between range and xrange is that the range function returns a new list with numbers of that specified range, whereas xrange returns an iterator, 
which is more efficient. """


#for x in range(2,5):
#    print(x)

#for x in range(7,10,2):
#    print(x)


"""'while' Loops"""
"""While loops repeat as long as a certain boolean condiiton is met."""

#count = 0

#while count < 5:
#    print(count)
#    count +=1

"""break and continue statements"""
"""break is used to exit a for loop or a while loop, whereas continue is used to skip the current block, and return to the "for" or "while" statement."""

#count = 0
#while True:
#    print(count)
#    count +=1
#    if count >= 1000:
#        break

"""only odd numbers:"""

#for x in range(10):
#    if x % 2 == 0:
#        continue

#    print(x)

"""only even numbers:"""
#for x in range (10):
#    if x % 2 == 1:
#        continue
#    print(x)

"""else"""

#count = 0

#while count < 5:
#    print(count)
#    count +=1
#else:
#    print("count value reached %d" %(count))


#for i in range(1, 10):
#    if (i%5==0):
#        break
#    print(i)

#else:
#    print("this is not printed because for loop is terminated because of break but not due to fail in condition.")

"""exercise"""

#numbers = [
#    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
#    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
#    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
#    743, 527
#]

#for number in numbers:
#    if number == 237:
#        break

#    if number % 2 == 1:
#        continue

#    print(number)



"""functions"""
"""Functions are a convenient way to divide your code into useful blocks, allowing us to order our code, make it more readable, reuse it and save some time. 
Also functions are a key way to define interfaces so programmers can share their code."""


#def my_Function():
#    print("hello my func")



#def my_function_with_args(username, greeting):
#    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

#my_function_with_args("fatih", "a great year")


"""exercise"""

#def list_benefits():
#    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"


#def build_sentence(benefit):
#    return "%s is a benefit of functions!" % benefit


#def name_the_benefits_of_functions():
#    list_of_benefits = list_benefits()
#    for benefit in list_of_benefits:
#        print(build_sentence(benefit))

#name_the_benefits_of_functions()

"""Class and Objects"""
"""Objects are an encapsulation of variables and functions into a single entity. Objects get their variables and functions from classes. 
Classes are essentially a template to create your objects."""

#class MyClass:
#    variable = "blah"

#   def function(self):
#        print("this message inside the class.")


#myobjectx = MyClass()

#print(myobjectx.variable)



#class MyClass:
#    variable = "blah"
#    def function(self):
#        print("this message inside the class.")


#myobjectz = MyClass()
#myobjectb = MyClass()


#myobjectz.variable = "yackity"

#print(myobjectb.variable)
#print(myobjectz.variable)

"""Accessing Object Functions"""
"""to access a function inside of an object you use notation similat to accessing a variable:"""

#class MyClass:
#    variable = "blah"

#    def function(self):
#        print("this is a message inside the class.")

#myobjectx = MyClass()

#myobjectx.function()


"""init()"""

#class NumberHolder:

#   def __init__(self, number):
#       self.number = number

#   def returnNumber(self):
#       return self.number

#var = NumberHolder(7)
#print(var.returnNumber()) 


"""exercise"""

#class Vehicle:
#    name = ""
#    kind = "car"
#    color = ""
#    value = 100.00
#    def description(self):
#        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
#        return desc_str


#car1 = Vehicle()
#car1.name = "Fer"
#car1.color = "red"
#car1.kind = "convertible"
#car1.value = 60000.00

#car2 = Vehicle()
#car2.name = "Jump"
#car2.color = "blue"
#car2.kind = "van"
#car2.value = 10000.00

#print(car1.description())
#print(car2.description())







print("hello world")



    

