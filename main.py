def add(*args):
    return sum(args)

def subtract(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result


def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def divide(*args):
    if 0 in args[1:]:
        raise ZeroDivisionError("Cannot divide by zero")
    result = args[0]
    for num in args[1:]:
        result /= num
    return result