#  the parameter in the read method, just specifies the number fo characters to be read
#  read 1 single line using readline method
# NOTE - if you do not comment print(file.read(12)) then the next line would start printing
# from the point where the previous line read ended.

# file = open("Test.txt")
# print(file.read(12))
# print(file.readline())
# print(file.readline())

# Question - Print all lines in the file line by line using readline method
# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()

# print(file.readlines())
with open("Test.txt", 'r') as reader:
    content = reader.readlines()
    with open("Test.txt", 'w') as writer:
        for line in reversed(content):
            writer.write(line)

