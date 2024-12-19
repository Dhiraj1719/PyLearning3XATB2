#*args - we can add any number of arguments
print("dhiraj","Bhavana", "amisha")
# def add(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     return sum
# print(add(1,2,3,4,5,6,7,8,9,10))

def sum_three(a,b,c):
    return a+b+c
print(sum_three(10,20,30))
print(sum_three(a=10, b=20, c=30))
print(sum_three(b=10, c=20, a=30))
print(sum_three(c=10, a=20, b=30))
print(sum_three(c=10, b=20, a=30))
print(sum_three(a=100, c=201, b=302))
