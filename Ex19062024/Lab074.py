numbers = [1,2,3,4] #list --> collections of items


def do_something (numbers):
    numbers.append(5)
    return numbers

change = do_something(numbers)
print(change)