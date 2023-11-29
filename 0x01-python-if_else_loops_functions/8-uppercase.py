#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        uppercase_char = chr(ord(char) - (ord('a') - ord('A'))) if 'a' <= char <= 'z' else char
        print("{}".format(uppercase_char), end="")
    print()
