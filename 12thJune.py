"""
Assignment Operators:

1) = 
2) += ----> a += 5 ----> a = a + 5
3) -=
4) *=
5) /=
6) //=
7) %=
8) **=
"""

# a = 5
# print(a)
# a += 5  # a = a + 5 ---> 5 + 5 =10
# print(a)
# a -= 2  # a = 10 - 2 ---> 8
# print(a)
# a *= 2 # 8 * 2 =16
# print(a)

# num1 = 15
# num2 = 12

# if num1 > num2:
#     print(num1,"is maximum")
# else:
#     print(num2,"is maximum")


# print(num1,"is maximum") if num1> num2 else print(num2,"is maximum")

"""
Bitwise Operators

1) & - Bitwise and

Truth Table

a   b   a&b
0   1   0
0   0   0
1   0   1
1   1   1   

48-    1    1   0   0   0   0
       &    &   &   &   &   &
45  -  1    0   1   1   0   1
    -------------------------------
        1     0   0    0    0    0
2) | - OR OPerator
a   b   a|b
0   0   0
0   1   1
1   0   1
1   1   1
48-    1    1   0   0   0   0
       |    |   |   |   |   |
45  -  1    0   1   1   0   1
    -------------------------------
       1    1   1   1   0   1




3) ^
4) <<
5) >>
"""

print(48&45)
print(48|45)
"""
75 & 65
89 & 16
23 & 12
44 | 35
32 | 19
95 | 36 
"""