"""This function adds 'ing' to the words"""
import re


def check_input(string):
    """This function checks user input for letters and spaces and returns True or False"""
    return re.fullmatch(r'[A-Za-z\s]*', string)


def add_ing(string):
    """This function splits string and adds 'ing' to the words"""
    sentence = []
    words = string.split()
    for word in words:
        sentence.append(word + 'ing')
    return " ".join(sentence)


def main():
    """This is the main function"""
    user_input = input('Enter your word or phrase(only english letters and spaces): ')
    valid_user_input = check_input(user_input)
    if valid_user_input:
        end = add_ing(user_input)
        print(end)
    else:
        print('Sorry, you input incorrect. Use only english letters and spaces.')


if __name__ == "__main__":
    main()
