# myTuple = ("apple","banana","cherry","mango")

# *green , red , yellow  = myTuple

# print(green)
# print(red)
# print(yellow)

# Dict1 = {
#     "a":{
#         1 : 56,
#         2 : 45,
#         3 : 31
#     },
#     "b":{
#         "x":"cherry"

#     }
# }
# print(Dict1)


# def myfunction():
#      print("Hello World")

# myfunction()

# def myfunc(x,y):
#       return x + y

# print(myfunc(4,6))

# def my_function(*kids):
#       print("child name:",kids[3])

# my_function("Emi","Linus","Hey",52)

# def my_function(child1,child2):
#       print("child name:",child2)

# my_function(child2="Emi",child1="Hey")

# def func(**name):
#       print("My name is:",name["fname"])

# func(fname="Emi" , lname="Emily")

# def func(fruits):
#       for x in fruits:
#           print(x)

# f = ("apple","banana","mango","cherry")

# func(f)


# x = lambda a,b,c,d,e: a + b + c + d + e

# print(x(4,3,2))

# def func(n):
#        return lambda a: a * n

# double = func(2)
# triple = func(3)
# print(double(11))
# print(triple(11))


class Person:
      def __init__(self,name,age,birthyear):
          self.name = name
          self.age = age
          self.birthyear = birthyear

      def func(self):
          print("Hello My name is :",self.name)

p1 = Person("Emi",26,2004)

print(p1.name)
print(p1.age)
print(p1.birthyear)
p1.func()

class Student(Person):
     def __init__(self, name, age,birthyear):
          super().__init__(name, age,birthyear)

x = Student("John",14,2005)
print(x.name)
print(x.age)
print(x.birthyear)
x.func()

