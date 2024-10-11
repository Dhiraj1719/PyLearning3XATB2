#strings
#bunch of char
#'', "","""
from Ex05062024.Lab0002 import first_name

name = "John"
print(name)
print(type(name))

name = 'John'
print(name)
print(type(name))


name = """John is good boy"""
print(name)
print(type(name))

#Raw String - when we have to give path then we use raw string
dir =r"C:\Users\chava\PycharmProjects\PyLearning3XATB2\Ex07062024"
print(dir)

#fromate of the string
first_name = "Dhiraj"
last_name = "Chavan"
print(first_name+ " " + last_name)
print(first_name, last_name)
#f - formatting string literal/variables
#{} --> palceholders
print(f"my name is {first_name} {last_name}")
print(f"{first_name} {last_name}")