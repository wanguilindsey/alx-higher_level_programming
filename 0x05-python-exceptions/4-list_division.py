#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            # Try to perform the division
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            # Handle division by zero
            print("division by 0")
            result = 0
        except TypeError:
            # Handle wrong type
            print("wrong type")
            result = 0
        except IndexError:
            # Handle out of range
            print("out of range")
            result = 0
        finally:
            # Append the result to the result_list
            result_list.append(result)

    return result_list
