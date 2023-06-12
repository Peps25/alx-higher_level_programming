#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)

    big = my_list[0]
    for ui in range(len(my_list)):
        if my_list[ui] > big:
            big = my_list[ui]

    return (big)
