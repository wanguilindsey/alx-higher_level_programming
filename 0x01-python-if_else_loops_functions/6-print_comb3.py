#!/usr/bin/python3
for a in range(10):
    for b in range(a + 1, 10):
        if a * 10 + b < 89:
            print("{:d}{:d}, ".format(a,b), end='')
        else:
            print("{:d}{:d}".format(a,b))
