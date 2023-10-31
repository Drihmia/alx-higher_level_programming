#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number:
    print("{0:=-d} is {1}".format(number,
                                  "negative" if number < 0 else "positive"))
else:
    print("{} is zero".format(number))
