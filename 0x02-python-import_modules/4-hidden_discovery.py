#!/usr/bin/python3.8

if __name__ == "__main_":
    import hidden_4
    for en in dir(hidden_4):
        if en[0].isalpha():
            print("{0:s}".format(en))
