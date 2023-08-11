#!/usr/bin/python3
<<<<<<< HEAD
for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")

=======
print(", ".join("{:02}".format(i) for i in range(100)))
>>>>>>> cdec887f77613d69d8107433ebf5f7871f48c5dc
