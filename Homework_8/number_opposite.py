"""This function print opposite number"""


def number_opposite(n, first_number):
    """This function print opposite number"""
    if first_number > n/2:
        print(round(first_number + (n/2) - n))
    else:
        print(round(first_number + (n/2)))


number_opposite(10, 9)
