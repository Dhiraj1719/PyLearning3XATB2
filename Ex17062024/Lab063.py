# args - is very similar to list but it is immutable
# def myfunc(*args):
#     print(args)
#     print(sum(args))
# myfunc(1,2,3,4,5,6,7,8,9,10)

def print_arguments(*args):
    for i in args:
        print(i, end="\n")


print_arguments( "amit", "amisha", "Dhiraj")

#args - is nothing but list
a = ["Dhiraj", "Bhavna", "Amisha", "lucky"]
for i in a:
    print(i, end=" \n")

for i in range(0, 10):
    print(i, end=" \n")