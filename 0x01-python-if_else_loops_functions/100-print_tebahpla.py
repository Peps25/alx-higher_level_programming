#!/usr/bin/python3
# 100-print_tebahpla.py

""""Print the alphabet in reverse order alternating upper- and lower-case."""
ui = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - ui)), end="")
    ui = 32 if ui == 0 else 0
