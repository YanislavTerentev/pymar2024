"""This program calculates the letter count"""


def calculate_letters_count(string):
    """This function calculates the letter count"""
    max_index = len(string) - 1
    result_string = ''
    count = 1
    for index, letter in enumerate(string):
        if index != max_index and letter == string[index + 1]:
            count += 1
        else:
            result_string += letter
            if count > 1:
                result_string += str(count)
            count = 1

    return result_string


assert calculate_letters_count("cccbba") == "c3b2a", "error"
assert calculate_letters_count("abeehhhhhccced") == "abe2h5c3ed", "error"
assert calculate_letters_count("aaabbceedd") == "a3b2ce2d2", "error"
assert calculate_letters_count("abcde") == "abcde", "error"
assert calculate_letters_count("aaabbdefffff") == "a3b2def5", "error"
