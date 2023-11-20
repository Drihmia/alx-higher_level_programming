#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if x < 0:
            raise IndexError()
        for i, ele in enumerate(my_list):
            print("{}".format(ele), end = "")
            if (i + 1 == x):
                break
        print()
        return i + 1
    except IndexError as e:
        print(e)
        return 0
    except Exception as e:
        print(e)
        return 0
