def calculate(exp):
    try:
        output = eval(exp)
        return output

    except ZeroDivisionError:
        return "Division by zero is forbidden."

    except NameError:
        return "Oops! Something went wrong. Maybe it's not a number"

    except SyntaxError:
        return "Syntax error. Try again."


while True:
    user_input = input('~')
    if user_input == 'done':
        break
    print(calculate(user_input))
