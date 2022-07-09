# Str1 = "Hello"

# print(Str1)
# print(Str1.lstrip())
# print(Str1.rstrip(),end="")
# print("Hey")
# print(Str1.strip())

# print(Str1.ljust(10),end="")
# print("Hey")
# print(Str1.rjust(10))

"""
List = Ordered & Mutable
# """

# myList =  ["Royal",12,52.25,2+5j]

# print(type(myList))

# print(myList)

# List1 = [5,4,3,2,67,89,54,90,12,54,52]
# print(max(List1))
# print(min(List1))
# print(sorted(List1))
# print(sum(List1))
# print(len(List1))

# print(List1[2])
# print(List1[-1])
# print(List1[0:6])
# print(List1[::-1])

# List2 = ["apple","Apple","banana","Cherry","mango","berry"]

# print(max(List2))
# print(min(List2))
# print(sorted(List2))
# print(sum(List2))

# list1 = [34,56,78,90,12,34,32,34,54,65,76,8798]

# list1.append(2)
# print(list1)


# list2 = []

# list2.append(int(input("Enter element")))
# list2.append(int(input("Enter element")))
# list2.append(int(input("Enter element")))
# list2.append(int(input("Enter element")))
# list2.append(int(input("Enter element")))

# print(list2)
list1 = [34,56,78,90,12,34,32,34,54,65,76,8798]

print(list1.count(34))

list2 = list1.copy()
print(list2)

list3 = list1
print(list3)

print(id(list1))
print(id(list2))
print(id(list3))

print(list1 is list2)
print(list1 is list3)

list2.clear()
print(list2)

# del list2
# print(list2)

list1 = [34,56,78,90,12,34,32,34,54,65,76,8798]

# list1.extend(list3)

# print(list1)
# print(list3)

# print(id(list1))
# print(id(list3))

print(list1.index(90))

list1.insert(7,56)
print(list1)

print(list1.pop(3))
print(list1)

list1.remove(76)
print(list1)

print(list1.reverse())
print(list1)

list1.sort()
print(list1)

