#Problem to find max in between 3 numbers
# '''a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=int(input("Enter third number: "))
# if a>b and a>c:
#     print(a,"is greater")
# elif b>a and b>c:
#     print(b,"is greater")
# else:
#     print(c,"is greater")'''

num1 = int(input("enter the first number : "))
num2 = int(input("enter the second number : "))
num3 = int(input("enter the third number : "))
# if num1>num2 and num1 > num3:
#     print("num1 is greater")
# elif num2 > num1 and num2 > num3 :
#     print("num2 is greater")
# else:
#     print("num3 is greater")

result = max(num1,num2,num3)
print("max value is : " , result)