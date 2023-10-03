#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    for k in range(len(str)):
        if k != n:
            s = s + str[k]
    return (s)
