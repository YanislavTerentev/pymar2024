"""This function defines the sequence"""


def compare_elements(copy_array):
    """This function compares the elements of a list"""
    for i in range(len(copy_array) - 1):
        if copy_array[i] >= copy_array[i + 1]:
            return False
    return True


def solution(array):
    """This function defines the sequence"""
    result = False
    if compare_elements(array):
        result = True
    else:
        for i in range(len(array)):
            copy_array = array.copy()
            del copy_array[i]
            if compare_elements(copy_array):
                result = True
                break
    return result


assert solution([1, 2, -3]) is True, "Solution failed"
assert (solution([1, 2, 1, 2])) is False, "Solution failed"
assert (solution([1, 3, 2, 1])) is False, "Solution failed"
assert (solution([1, 2, 3, 4, 5, 3, 5, 6])) is False, "Solution failed"
assert (solution([40, 50, 60, 10, 20, 30])) is False, "Solution failed"
