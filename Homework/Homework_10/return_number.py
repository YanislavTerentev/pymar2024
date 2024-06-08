ERROR_MESSAGE = 'Error! Function result is not number.'


def is_number(func):
    def wrapper(sting):
        result = func(sting)
        if not isinstance(result, float):
            print(ERROR_MESSAGE)
            return ERROR_MESSAGE
        return result
    return wrapper


@is_number
def checking_strung(sting):
    try:
        float(sting)
        s = float(sting)
        return s
    except ValueError:
        return sting


assert checking_strung('5.5') == 5.5, "Result should be 5.5"
assert checking_strung('5') == 5.0, "Result should be 5.0"
assert checking_strung('text') == ERROR_MESSAGE, "Result should be a number"
