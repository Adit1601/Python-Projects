def greetme(name):
    print("Hello "+name)

def add(a,b):
    return a+b

name1 = input("Enter username \n")
greetme(name1)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))

ans = add(num1,num2)
print(ans)

str = "AditShahAcademy"
str1 = ".com"
str2 = "AditShah"
str4 = " Adit "
str3 = str+str1
print(str[1]) #d
print(str[0:4]) #Adit
print(str+str1) # AditShahAcademy.com
print(str2 in str) # True
print(str.__contains__(str2)) #True
print(str3.split("."))
print(str3.split(".")[0]+" "+str3.split(".")[1]) #AditShahAcademy com
print(str4.strip())
print(str4.lstrip())
print(str4.rstrip())
