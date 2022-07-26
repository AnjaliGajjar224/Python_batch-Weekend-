"""
Anjali Rakesh Gajjar
"""

# name = input("Enter your Full Name(firstname+middlename+lastname):")

# print(name[0],".",name[name.index(" ")+1],".",name[name.rindex(" ")+1:])

# part1 = name[0]
# part2 = name[name.index(" ")+1]
# part3  = name[name.rindex(" ")+1:]

# print(part1)
# print(part2)
# print(part3)

# print(part1+"."+part2+"."+part3)

"""
tuples - immutable & ordered
# """
# myTuple = (1,2,3,4,5)
# print(myTuple)
# print(type(myTuple))

# t1 = 1,2,3
# print(type(t1))

# t2 = (21,)
# print(type(t2))

# t3 = ("Royal",)
# print(type(t3))

# print(myTuple[0])
# print(myTuple[-1])

# for i in myTuple:
#     print(i)

# tup = (1,23,45,65,78,98,100,43,32,23)

# print(tup.count(23))
# print(tup.index(23))

# print(tup[2])

# # tup[2] = 100
# print(tup)

# l1 = list(tup)

# l1.append(100)
# print(l1)

# tup = tuple(l1)
# print(tup)

# print(max(tup))
# print(min(tup))
# print(sum(tup))
# print(len(tup))
# print(sorted(tup))
# print(sorted(tup,reverse=True))

"""
unpacking tuple
"""

tup = ("apple","banana","cherry","berry","mango","pineapple")

# b1 , b2 , b3 , b4 , b5 = tup

# print(b1)
# print(b2)
# print(b3)
# print(b4)
# print(b5)
# print(b6)

# b1 , b2 , *b3 = tup

# print("First element:",b1)
# print("Second element:",b2)
# print(b3)

b1 , *b2 , b3 = tup

print("First element:",b1)
print("Second element:",b2)
print("Last element:",b3)

*b1 , b2 , b3 = tup

print("First element:",b1)
print("Second Last element:",b2)
print("Last element:",b3)

l1 = [("apple",12),("banana",13),("cherry",14),("berry",15),("mango",16),("pineapple",17)]
print(l1)

# t1 = ([12,23])

# print(t1)