"""Print "*" pyramid"""


def create_pyramid(count):
    """This function prints a pyramid"""

    for i in range(count):
        print(' ' * (count - i - 1), end='')
        print('*' * (2 * i + 1))


create_pyramid(10)
