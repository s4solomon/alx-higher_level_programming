#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx is >= 0 and idx < len(my_list):
        my_list[idx] = element
    else:
        return(my_list)
