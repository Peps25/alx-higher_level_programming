#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    ret = 0
    for ui in range(0, x):
        try:
            print("{:d}".format(my_list[ui]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
