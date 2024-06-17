def typed(type_element):
    def convert(func):
        def wrapper(*args):
            formatted_array = []
            for arg in args:
                if isinstance(arg, type_element):
                    formatted_array.append(arg)
                else:
                    formatted_array.append(type_element(arg))
            return func(*formatted_array)
        return wrapper
    return convert


@typed(type_element=str)
def add1(a, b):
    return a + b


assert add1("3", 5) == '35'
assert add1(5, 5) == "55"
assert add1('a', 'b') == 'ab'


@typed(type_element=int)
def add2(a, b, c):
    return a + b + c


assert add2(5, 6, 7) == 18


@typed(type_element=float)
def add3(a, b, c):
    return a + b + c


assert add3(0.1, 0.2, 0.4) == 0.7000000000000001
