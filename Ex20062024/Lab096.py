# Decorators -  Decorators in Python are a powerful and flexible tool that allows
#  you to modify the behavior of functions or methods without
#  changing their actual code



# They are essentially functions that take another function as an
#  argument and extend or alter its behavior

def my_decorator(func):

    def wrapper():
        print("starting.......")
        print("***************")
        func()
        print("**************")
        print("ending.....")

    return wrapper()


@my_decorator
def say_hello():
    print("say hello")

#say_hello()
