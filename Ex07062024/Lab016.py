#Take 2 number and we have to add them


num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
#print (add_two_numbers(num1, num2))
"""result = num1 + num2
print(result)"""
# input method always take value as string so we have to typecast it into int
result = int(num1) + int(num2)
print(result)

#+ -> int --> addition
#+ -> str --> concatenation
#Conversion function
# int to str --> str()
#str to int --> int()