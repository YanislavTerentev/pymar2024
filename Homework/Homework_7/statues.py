"""Print number of statues"""


def statues_number(statues):
    """function checks how much statues needed to make whole line"""
    statues_ordered = sorted(statues)
    all_statues = list(range(statues_ordered[0], statues_ordered[-1] + 1))
    return len(all_statues) - len(statues_ordered)


statues_li = [1, 2, 3]
print(statues_number(statues_li))
