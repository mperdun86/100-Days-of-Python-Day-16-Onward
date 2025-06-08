def logging_decorator(function):
    def wrapper(*args):
        result = function(*args)
        name = function.__name__
        arguments = args
        print(F"You called {name}{arguments}\nIt returned: {result}")
        return result
    return wrapper

@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)