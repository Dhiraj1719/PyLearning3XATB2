def decorator1(func):
    def wrapper():
        print("decorator1")
        return func()  # Ensure that we return the actual function result
    return wrapper  # Return the wrapper function

def decorator2(func):
    def wrapper():
        print("decorator2")
        return func()  # Ensure that we return the actual function result
    return wrapper  # Return the wrapper function

@decorator1
@decorator2
def say_hello():
    print("hello")

say_hello()

