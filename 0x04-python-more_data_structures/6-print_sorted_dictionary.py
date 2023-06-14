#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    for ui in list_ord:
        print("{}: {}".format(ui, a_dictionary.get(ui)))
