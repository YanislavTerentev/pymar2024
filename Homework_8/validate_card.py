"""This program validate card"""
import re


def check_number_number(number_number):
    return re.fullmatch(r'[0-9]{13,16}', number_number)


def validate_number():
    number_number = input('Enter a card number: ')
    number_validate = check_number_number(number_number)
    card_numbers_sum = 0
    if not number_validate:
        print('Invalid card number')
    else:
        arr = list(map(int, number_number))
        arr.reverse()
        for index, number in enumerate(arr, start=1):
            if index % 2 == 0:
                number *= 2
                if number > 9:
                    number -= 9
            card_numbers_sum += number
        if card_numbers_sum % 10 == 0:
            print('Card is valid')
        else:
            print('Card is invalid')


validate_number()
