#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for m in my_list[:x]:
            print("{}".format(m), end="")
            count += 1
    except:
        pass
    print()
    return count
