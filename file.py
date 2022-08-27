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

f = open("data.txt", "x")

for i in range(5):
    f.write(input("Enter data: "))

f = open("data.txt", "r")

print(f.read())

f.close()