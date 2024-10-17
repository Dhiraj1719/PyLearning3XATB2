#operators

#= --> Assignment operator
age = 65
name = "pramod" #assign value from right to left
print(name)
print(age)

# == --> compare operator - compare two value (boolean)
v1 = ( 1 == True)
print(v1)

v2 = ( 0 == False)
print(v2)

'''1 --> true
0 --> false'''

#unary operator
age = +65
print(age)
num = -1
r = age +  num
print(r)

#not operator (only work with boolean)
is_married = True
print(not is_married)

#is operator - identity operator -- return bool
#is operator - compare memory location
a = 5
b = 5
print(a is b)
print(id(a))
print(id(b))
print(id(a) == id(b))
print(id(a) is id(b))
print(id(a) is not id(b))
print(id(a) == id(b))
print(id(a) is id(b))

