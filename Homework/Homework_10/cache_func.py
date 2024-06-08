def cache(func):
    cache_dictionary = {}

    def wrapper(arg):
        if arg in cache_dictionary:
            return cache_dictionary[arg]
        cache_dictionary[arg] = func(arg)
        return func(arg)

    return wrapper


@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


assert fibonacci(5) == 5, "Output should be 5"
assert fibonacci(10) == 55, "Output should be 55"
assert fibonacci(5) == 5, "Output should be 5"
