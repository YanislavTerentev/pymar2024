def validate_arguments(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int) or arg < 0:
                raise ValueError('Only positive integers are allowed')
        func(*args)
    return wrapper


@validate_arguments
def some_function(*args):
    print(args)


some_function(25, 10, 8513)
