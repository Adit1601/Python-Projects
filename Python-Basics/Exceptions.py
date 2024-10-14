ItemsInCart = 0

# if ItemsInCart!=2:
#     raise Exception("Product count not matching")

# assert(ItemsInCart!=0)

# try except final
try:
    with open("Test1.txt") as reader:
        content = reader.read()
        print(content)
# except FileNotFoundError:
#     print("File not found")
except Exception as ex:
    print(ex)
    print("Some other error occured")
finally:
    print("Finally block")