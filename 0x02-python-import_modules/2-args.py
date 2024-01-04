#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    if argc == 0:
        print("{} arguments.".format(argc))
    else:
        print("{} arguments:".format(argc))
        i = 1
        for arguments in argv[1:]:
            print("{}: {}".format(i, arguments))
            i += 1
