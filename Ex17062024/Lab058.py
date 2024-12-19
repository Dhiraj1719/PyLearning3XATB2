# function
# Block of code which is executed together and can be reusable
# Define and then call function
# builtin functions - which are created by python contributors.
# eg: print, max, min, add, range,input,type,id
# user defined functions - which are created by Users
# they can return something or they can not return anything
# they have parameters or don't have parameters.


def Say_hello():  # no arguments/parameter, no return type
    print("Hello")


Say_hello()


def Say_hello2(name):  # with parameter, no return type
    print("Hello", name)


Say_hello2("Dhiraj")


def Say_hello3(name="Dhiraj"):  # with parameter, no return type

    print("Hello", name)


Say_hello3("Bhavana")
Say_hello3()
Say_hello3(name="Arun")


def sum_number_arguments_ret(a, b):  # with return type with Return word

    return a + b


# result = sum_number_arguments_ret(10,20)
# result2 = sum_number_arguments_ret(145,20)
result = sum_number_arguments_ret(b=14, a=20)
print(result)
