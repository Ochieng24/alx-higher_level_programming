#!/usr/bin/python3
<<<<<<< HEAD
# 7-islower.py


def islower(c):
    """Check for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False

=======
def islower(c):
    if 97 <= ord(c) <= 122:
        return True
    else:
        return False
>>>>>>> cdec887f77613d69d8107433ebf5f7871f48c5dc
