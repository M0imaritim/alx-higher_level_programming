#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    n = len(argv) - 1
    sum = 0
    if n == 0:
        sum += 0
        print("{}".format(sum))
    else:
        for arg in argv[1:]:
            sum += int(arg)
        print(sum)
