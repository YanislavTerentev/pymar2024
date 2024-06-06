"""This program delete "#" and symbol before"""


def delete_symbol(string):
    """This function delete "#" and symbol before"""
    new_list = list(string)
    index = 0
    while index < len(new_list):
        if new_list[index] == "#":
            new_list.pop(index)
            if index != 0:
                new_list.pop(index - 1)
                index -= 1
        else:
            index += 1

    return "".join(new_list)


assert delete_symbol("a#bc#d") == "bd", "error"
assert delete_symbol("abc#d##c") == "ac", "error"
assert delete_symbol("abc##d######") == "", "error"
assert delete_symbol("#######") == "", "error"
assert delete_symbol("") == "", "error"
