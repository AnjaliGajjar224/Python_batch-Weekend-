"""
1) Factorial of a number
2) Fibonacci series

e.g. 0 1 1 2 3 5 8 13 21 34 55 89

3) Prime number
4) Palindrome number
"""

"""
Nested Loops:
------------------------
initialization

while condition:
    initialization
    while condition:
        code
        increment/decrement
    increment/decrement
"""
# i = 1

# while i <= 5:
#     j = 1
#     while j <= 5:
#         print("*",end=" ")
#         j += 1
#     print()
#     i += 1

"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
"""

# i = 1
# num = 1
# while i <= 5:
#     j = 1
#     while j <= 5:
#         print(num,end=" ")
#         num += 1
#         j += 1
#     print()
#     i += 1

"""
while ...else
"""

i = 7

while i <= 5:
    print(i,end=" ")
    i += 1

else:
    print("Condition is not True")