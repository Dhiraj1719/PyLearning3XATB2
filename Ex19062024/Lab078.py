#lambda arguments : Expression
#
#
# def find_even_odd (num):
#     if (num%2 == 0):
#         print("even")
#     else:
#         print("odd")
#
# find_even_odd(10)
#

#Lambda function ---------------
# function name  = lambda arguments : operation
# print(function name (arguments values

find_even_odd = lambda num : "even" if (num%2==0) else "odd"
print(find_even_odd(19))