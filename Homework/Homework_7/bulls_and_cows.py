import random


def generate_digit():
    """function generating a number of 4 random unique digits"""
    number = []
    while len(number) < 4:
        digit = random.randint(0, 9)
        if digit not in number:
            number.append(digit)
    return number


def trying_guess():
    """function asking user to enter their guess and checking it"""
    try:
        first_guess = int(input('Input your digit: '))
    except ValueError:
        print('Invalid input. Please enter only digits')
        result = trying_guess()
    else:
        if len(list(map(int, str(first_guess)))) != 4:
            print('Invalid input. Please enter 4 unique digits')
            result = trying_guess()
        if len(set(map(int, str(first_guess)))) != 4:
            print('Invalid input. Please enter 4 unique digits')
            result = trying_guess()
        else:
            result = list(map(int, str(first_guess)))
    return result


def bulls_and_cows_game(answer, guess):
    """function describing 'cows and bulls' game"""
    cows = 0
    bulls = 0
    result = ''
    for i in range(4):
        if guess[i] == answer[i]:
            bulls += 1
        elif guess[i] in answer:
            cows += 1
    print(f'{cows} cows, {bulls} bulls')
    if bulls == 4:
        result = print('Congratulations! You win!')
    if bulls != 4:
        guess = trying_guess()
        result = bulls_and_cows_game(answer, guess)
    return result


generated_answer = generate_digit()
user_guess = trying_guess()
bulls_and_cows_game(generated_answer, user_guess)