#!/usr/bin/python3
<<<<<<< HEAD
for letter in range(97, 123):
    if chr(letter) is not 'q' and chr(letter) is not 'e':
        print("{}".format(chr(letter)), end="")

=======
for char in range(97, 123):
    if char == ord('e') or char == ord('q'):
        continue
    print("{}".format(chr(char)), end='')
>>>>>>> cdec887f77613d69d8107433ebf5f7871f48c5dc
