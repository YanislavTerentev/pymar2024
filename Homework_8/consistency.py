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
    print(result)


solution([1, 2, 3])
solution([1, 2, 1, 2])
solution([1, 3, 2, 1])
solution([1, 2, 3, 4, 5, 3, 5, 6])
solution([40, 50, 60, 10, 20, 30])
