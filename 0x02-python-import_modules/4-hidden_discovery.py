#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    i = 0
    for i in dir(hidden_4):
        if i[0] != "__" and i[1] != "__":
            print(i)
