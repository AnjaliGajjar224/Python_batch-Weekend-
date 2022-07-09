"""
Bitwise Operators

3)XOR(Exclusive OR) - ^

a   b   a^b
0   0   0
1   1   0
0   1   1
1   0   1

48-    1    1   0   0   0   0
       ^    ^   ^   ^   ^   ^
45  -  1    0   1   1   0   1
    -------------------------------
       0    1   1   1   0   1

78^49
47^16
38^29




# """
# print(48^45)
# print(78^49)
# print(47^16)
# print(38^29)

# print(15<<2)
# print(15>>2)
# print(15<<3)
# # print(15>>2)
# print(20<<4)
# print(23>>2)
# print(75<<6)
# print(16>>3)


"""
Logical Operators

1)and
2)or
3)not

"""

# a = 15
# b = 12
# c = 16

# print(a>b and a>c)      # True(1) and False(0) ----> False(0)
# print(a>b or a>c)       # True
# print(not(a>b))         #not(True) ---> False

"""
Membership Operators

1) in
2) not in

for ---> Syntax different 
"""

# print('b' in 'banana')
# print('k' in 'banana')

# print('b' not in 'banana')
# print('k' not in 'banana')

"""
Identity Operators

1) is
2) is not
"""

a = 19
b = 20
c = 19
d = 21

print(id(a))
print(id(b))
print(id(c))
print(id(d))

print(a is b)
print(a is c)
print(a is not b)
print(a is not c)