"""This program validate card"""
import re


def check_number_number(number_card):
    """This unction checks card number"""
    return re.fullmatch(r'[0-9]{13,16}', number_card)


def validate_number(number_card):
    """This program validate card"""
    number_validate = check_number_number(number_card)
    card_numbers_sum = 0
    if not number_validate:
        print('Invalid card number')
    else:
        arr = list(map(int, number_card))
        arr.reverse()
        for index, number in enumerate(arr, start=1):
            if index % 2 == 0:
                number *= 2
                if number > 9:
                    number -= 9
            card_numbers_sum += number
        return card_numbers_sum % 10 == 0


user_input = input('Enter a card number: ')
assert (validate_number(user_input)) is True, "Invalid card number"
