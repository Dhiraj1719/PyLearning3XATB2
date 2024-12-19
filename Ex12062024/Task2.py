# # # 1 to find leap year
# # # divisible by 4 and 400
# # Year = int(input("Enter the year: "))
# # if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
# #     print("Yes, It is Leap Year")
#
# #2 Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
# a = int(input("Enter the length of side 1: "))
# b = int(input("Enter the length of side 2: "))
# c = int(input("Enter the length of side 3: "))
# if a == b == c:
#     print("triangle is Equilateral triangle")
#     #all sides are equal
# elif a == b or b == c or c == a:
#     print("triangle is Isosceles triangle")
#     #exactly two sides are equal
# else:
#     print("triangle is Scalene triangle")
#
#
# # Task 3- Fibonacci series and Factorial
#
#
# # 3. Factorial
# # 5! = 5*4*3*2*1 -> 120
# # 4! = 4*3*2*1 -> 24
# # 3! = 3*2*1 -> 6
# # 2! = 2*1 -> 2
# # 1! = 1 -> 1
# # 0! = 1 -> 1
#
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
import math
#
# n = 5
# factorial = 1
# for i in range(1, n + 1):
#     factorial = factorial * i
#     print(factorial)
#OR

n=5
factorial = 1
# result = math.factorial(5)
# print (result)

while n>0:
    factorial = factorial *n
    factorial *= 1
    print(factorial)
# 5! -->5*4*3*2*1 -> 120

# 3! -> 3*2*1 -> 6

# 4! -> 4*3*2*1 -> 24
