# for i in range(n):
#     print(i)


# x = [i for i in range(5) if i % 2 == 0]

# print(x)

tupList = [("4", "645"), ("python","54"), ("1921", "431"), ("includehelp", "90")]
print("The initial tuple list is " + str(tupList))

# Extracting all tuples which have numeric strings 
numTupList = [tup for tup in tupList if all(vals.isdigit() for vals in tup)]

# Printing extracted list 
print("List of tuples with all elements of list that are Numeric string : " + str(numTupList))


"""
Take two string as an input from the user and Check whether the string is anagram or not.

e.g.

Input:
s1 = listen          [l,i,s,t,e,n]

s2 = silent          [s,i,l,e,n,t]

Anagram = True

2) Input:
s1 = dad
s2 = bad

Anagram = False

"""