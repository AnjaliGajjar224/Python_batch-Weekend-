"""
Set - Set is a collection which is unordered and unindexed.

Set is mutable.

Set is used to store unique elements.

# """
# set1 = {1,2,3,4,5,1,2}

# print(type(set1))
# print(set1)
# print(len(set1))

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

set1.add(6)
print(set1)

set3 = set1.copy()
print(set3)

set3.clear()
print(set3)

# my_set = set()

# print(type(my_set))

del set3
# print(set3)

set1.discard(6)
print(set1)

print(set1.difference(set2))               # set1 - set2 = {1,2,3,4,5} - {4,5,6,7,8} = {1,2,3}

# set1.difference_update(set2)
# print(set1)

print(set2.difference(set1))

# print(set2)

print(set1.symmetric_difference(set2))    # {1,2,3,4,5} ^ {4,5,6,7,8} = {6,7,8}

# set1.symmetric_difference_update(set2)
# print(set1)

print(set1.intersection(set2))                  # {1,2,3,4,5} & {4,5,6,7,8} = {4,5}

# set1.intersection_update(set2)
# print(set1)

set3 = {1,2,3}
set4 = {4,5,6}
set5 = {1,2,3,4,5,6}

print(set3.isdisjoint(set4))                # Return boolean True if set3 and set4 have no common elements.
print(set3.isdisjoint(set5))

print(set3.issubset(set5))                  # Return boolean True if set3 is a subset of set5.
print(set3.issuperset(set4))                # Return boolean True if set3 is a superset of set4.

print(set5.issuperset(set4))

print(set1.pop())                                  # Remove and return an arbitrary element from set1.
print(set1)

set1.remove(4)                                    # Remove an element from set1.
print(set1)

set1.discard(5)
print(set1)


set1.discard(6)
print(set1)

# set1.remove(5)
print(set1)

print(set1.union(set2))                                  # Return a new set with elements from both set1 and set2.

set1.update(set2)
print(set1)


my_str = "Hello World"
my_set = set(my_str)

print(my_set)

"""
Take input string from the user.

Input: Hey! Good Morning

character: e , n , H

Output: Good

"""
myStr = input("Enter Your String:")

set1 = set()

for i in range(3):
    n = input("Enter Character:")
    set1.add(n)

# print(set1)

mylist = myStr.split(' ')
list1 = []
for i in mylist:
    for j in i:
        if j in set1:
            list1.append(i)
            break
       
# print(list1)

for i in mylist:
    if i not in list1:
        print(i)
