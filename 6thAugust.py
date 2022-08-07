"""
Dictionaries: unordered and mutable
# """
# set1 = set()
# myDict = {}

# print(type(set1))
# print(type(myDict))

"""
Dictionaries are Key , Value pairs.
"""




myDict = {
    "a":"apple",
    "b":"banana",
    "c":"Cherry"
}

print(myDict)
print(myDict["a"])
print(myDict["b"])
print(myDict["c"])


thisdict = {
    1: "Ridhang",
    2: "OM",
    3: "Hemangini"
}

print(thisdict[1])

print(thisdict.get(2))

print(thisdict.keys())

print(thisdict.values())

for i in thisdict.keys():
    print(thisdict.get(i))


x = "Key-1" , "Key-2" , "Key-3"
y = 0 , 1, 2
Dict1 = {}

print(Dict1.fromkeys(x,y))

print(thisdict.items())

print(thisdict.pop(3))
print(thisdict)

print(thisdict.popitem())
print(thisdict)

print(thisdict.setdefault("a","apple"))
print(thisdict)

print(thisdict.setdefault("a","banana"))
print(thisdict)

print(thisdict.update({"a":"banana"}))
print(thisdict)