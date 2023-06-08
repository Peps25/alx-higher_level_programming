#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = 0
    for ui in range(len(sys.argv) - 1):
        total += int(sys.argv[ui + 1])
    print("{}".format(total)
