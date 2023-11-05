#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        new_list = list(my_list)
        new_list[idx] = new_element
        return new_list
