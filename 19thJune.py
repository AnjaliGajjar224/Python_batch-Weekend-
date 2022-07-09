"""
Topic : String

--->Immutable
--->Ordered 
# # """
# Char = 'c'
# print(type(Char))

# print("Hello!!!")
# print('Good Evening')

# Str1 = "Hello"
# Str2 = 'HII'

# print(type(Str1))
# print(type(Str2))

"""
-->len(var_name)
"""
# myString = "Royal_Technosoft_Pvt_Ltd"
# print(len(myString))
"""
R   0   -24
o   1   -23
y   2   -22
a   3   -21
l   4   -20
_   5   -19
T   6   -18
e   7   -17
c   8   -16
h   9   -15
n   10  -14
o   11  -13
s   12  -12
o   13  -11
f   14  -10
t   15  -9
_   16  -8
P   17  -7
v   18  -6
t   19  -5
_   20  -4
L   21  -3
t   22  -2
d   23  -1

# """
# print(myString[0])
# print(myString[-1])
# print(myString[23])
# print(myString[16])
# print(myString[24])

"""
Slicing

Syntax : var_name[start:end:step]
"""

from re import U


myString = "Royal_Technosoft_Pvt_Ltd"

# print(myString[0:15])
# # myString = myString[0:15]
# print(myString[2:10])
# print(myString)
# print(myString[-20:-2])
# # print(myString[:])
# print(myString[:15])
# # print(myString[5:])
# print(myString[23:5])
# print(myString[-1:-20])
# print(myString[:-3])
# print(myString[-16:])
# print(myString[5])

# Str1 = input("Enter String:")

# print("Length of String : ",len(Str1))

# s = int(input("Enter Starting index:"))
# e = int(input("Enter ending Index:"))

# print("Slicing of String is : ",Str1[s:e])

# myString = "Royal_Technosoft_Pvt_Ltd"
# print(len(myString))
# # print(myString[2:19:1])
# print(myString[2:19:2])
# print(myString[2:19:3])
# print(myString[::5])
# print(myString[2:19])

# print(myString[::-1])
# print(myString[-1:-16:-2])
# print(myString[19:1:-2])

# print(myString.center(44))                                  # 44 - len(string) = 20 ---> 20/2 = 10
# print(myString.capitalize())
# # print(myString)
# print(myString.casefold())
# print(myString.count('_'))
# print(myString.encode())


# if(myString == myString.encode()):
#     print("True")
# else:
#     print("False")

# str1 = "Good\tMorning\tHey"
#print(str1.expandtabs(10))
# print(str1.endswith('y'))

# myString = "Royal_Technosoft_Pvt_Ltd. since {year}"

# num1 = 15
# num2 = 20

# print(num1,"+",num2,"=",num1+num2)

# # print(f'{num1} + {num2} = {num1+num2}')
# print("Your age is : {age}".format(age = 18))

# print("My name is {name},I am {age} years old".format(name=input("Enter name:"),age=18))

# print(myString.format(year = 2015))

# myStr = "Royal_Technosoft_Pvt_Ltd"

# print(myStr.find('o'))
# print(myStr.rfind('o'))

# # print(myStr[::-1])

# print(myStr.index('o'))

# print(myStr.find('b'))
# print(myStr.index('b'))

# Str1 = "RoyalTechnosoft"
# Str2 = "123"
# # print(Str1.isalnum())
# print(Str1.isalpha())
# print(Str1.isascii())
# print(Str2.isdecimal())
# print(Str2.isnumeric())

# Str3 = "ROYAL TECHNOSOFT PVT LTD."
# print(Str3.isidentifier())
# print(Str3.islower())
# print(Str3.isupper())

# Str2 = "Are you \n#1?"
# print(Str2)
# print(Str2.isprintable())

# Str1 = "           "
# print(Str1.isspace())

# Str2 = "Royal Technosoft Pvt Ltd"
# print(Str2.istitle())

# Str3 = "Royal123"
# print(Str3.isalpha())

myString = "royal_technosoft_pvt_Ltd"
Str1 = "Hello"
print(myString.join(Str1))

print(myString.lower())
print(myString.upper())
print(myString.title())
print(myString.partition('_'))
print(myString.rpartition("_"))
print(myString.split('_'))
print(myString.replace('royal','loyal123'))

print(myString.rindex('o'))


Str2 = "1-06-2022"
print(Str2.zfill(10))            #5 - len(str) = 5 - 3 = 2