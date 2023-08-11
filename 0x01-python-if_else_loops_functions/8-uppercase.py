#!/usr/bin/python3
<<<<<<< HEAD
# 8-uppercase.py


def uppercase(str):
    """Print a string in uppercase."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")

=======
def uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print()
>>>>>>> cdec887f77613d69d8107433ebf5f7871f48c5dc
