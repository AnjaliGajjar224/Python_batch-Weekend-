"""
Comparison Operator

1) <
2) >
3) <=
4) >=
5) ==
6) !=

"""

# num1 = 4
# num2 = 6
# num3 = 9

# print(num1>num2)         # 4 > 6 -----> False
# print(num1<num3)         # 4 < 9 -----> True

# a = True
# b = False

# print(a)
# print(type(a))
"""
Condition Operators

if(condition)
{


}

if condition:
    //Operations


# """
# num1 = 9
# num2 = 10

# if num2 > num1:
#     print("num2 is greater ")
# else:
#     print("num1 is greater")

# num1  = int(input("Enter Number 1:"))
# num2 =  int(input("Enter Number 2:"))
# #print(type(num1))
# add = num1 + num2

# print(add)

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
num3 = int(input("Enter number 3:"))

if num1 > num2:
    if num1 > num3:
        print(num1,"is greater")

elif num2 > num3:
    print(num2,"is greater")

else:
    print(num3,"is greater")




