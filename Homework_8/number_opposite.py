"""This function print opposite number"""


def number_opposite(n, first_number):
    """This function print opposite number"""
    if first_number > n/2:
        return round(first_number + (n/2) - n)
    return round(first_number + (n/2))


print(number_opposite(10, 2))
