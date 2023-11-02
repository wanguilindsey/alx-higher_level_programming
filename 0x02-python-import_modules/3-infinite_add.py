#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    total = 0
    for arg in arguments:
        total += int(arg)
    print("{}".format(total))
