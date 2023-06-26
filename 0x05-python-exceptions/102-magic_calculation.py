#!/usr/bin/python3


def magic_calculation(a, b):
    result = 0
    for ui in range(1, 3):
        try:
            if ui > a:
                raise Exception('Too far')
            else:
                result += a ** b / ui
        except Exception:
            result = b + a
            break
    return (result)
