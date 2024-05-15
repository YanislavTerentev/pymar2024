"""This function adds 'ing' to the words"""
import re


def check_input(string):
    """Check user input for letters and spaces"""
    return re.fullmatch(r'[A-Za-z\s]*', string)


def add_ing(string):
    """Split string and adds 'ing' to the words"""
    sentence = []
    words = string.split()
    for word in words:
        sentence.append(word + 'ing')
    return " ".join(sentence)


def main():
    """This is the main function"""
    user_input = input('Enter your word or phrase(only letters and spaces): ')
    valid_user_input = check_input(user_input)
    if valid_user_input:
        end = add_ing(user_input)
        print(end)
    else:
        print('Use only english letters and spaces, please')


if __name__ == "__main__":
    main()
