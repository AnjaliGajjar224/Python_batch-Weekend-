"""
File Handling
--------------

    1. open() --- To open a file
    2. close() --- To close a file

r - Read only
w - Write only
a - Append
x - Create

Syntax:

    file_object = open(filename,mode)
"""

# Open a file


# f = open("demo.txt", "r")

# # print(f.read())

# print(f.readline())
# print(f.readline())

# f.close()

# f = open("demo.txt", "a")

# f.write("\nThis is a new data")

# f.close()

# f = open("demo2.txt", "x")    # x - Create

# f.write("New data")
# f.close()

# f = open("demo.txt", "w")

# f.write("Oops this is a new data")

# f.close()

# f = open("demo3.txt", "w")

# f.write("This is a new file")

# f.close()

# f = open("data.txt", "x")

# for i in range(5):
#     f.write(input("Enter data: "))

# f = open("data.txt", "r")

# print(f.read())

# f.close()

# f = open("data.txt", "w")

# for i in range(10):
#     f.write(input("Enter number: "))


# f = open("data.txt", "r")
# sum = 0
# m = f.read()
# e = open("even.txt", "w")
# o = open("odd.txt", "w")
# for i in m:
#     j = int(i)
#     if j % 2 == 0:
#         sum += j
#         e.write(i)
#     else:
#         print("Odd number:",j)
#         o.write(i)

# print("Addition of even numbers are: ",sum)

# f.close()
# e.close()
# o.close()

# f = open("data.txt", "r")

# with open("even.txt", "r") as f:
#     print(f.read())

# with open("f1.txt", "r") as f1:
#     data1 = f1.read()
# with open("f2.txt", "r") as f2:
#     data2 = f2.read()

# with open("final.txt","w") as f:
#     f.write(data1)
#     f.write(data2)




with open("final.txt","r") as f:
    data = f.readlines()

# count_upper = 0
# count_lower = 0
# count_digit = 0

# for ch in data:
#     if ch.isupper():
#         count_upper += 1
#     elif ch.islower():
#         count_lower += 1
#     elif ch.isdigit():
#         count_digit += 1

# print("Upper Case: ",count_upper)
# print("Lower Case: ",count_lower)
# print("Digits: ",count_digit)

count_lines = 0
count_A = 0
count_B = 0
count_C = 0

for line in data:
    count_lines += 1
    if line[0] == 'A':
        count_A += 1
    elif line[0] == 'B':
        count_B += 1
    elif line[0] == 'C':
        count_C += 1

print("Lines: ",count_lines)
print(count_A)
print(count_B)
print(count_C)

f.close()

"""
Replace all spaces from text with – (dash).
"""