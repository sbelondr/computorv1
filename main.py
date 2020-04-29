#!/usr/bin/python

import sys
# import array

def neutreEquation():
    pass

def positiveEquation():
    pass

def negativeEquation():
    pass

# later
def reduceForm():
    pass

def polynominale2():
    pass

def createArrEquation(arr):
    equation = [['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
    i = 0
    j = 0
    if arr[0] != "-" and arr[0] != "+":
        arr.insert(0, "+")
    for line in arr:
        equation[j][i] = line
        if i >= 3:
            i = 0
            j += 1
        else:
            i += 1
        if (j > 2):
            break
    return equation

def parseArg(arg):
    arr = arg.split()
    for line in arr:
        print(line)
    arr = createArrEquation(arr)
    return arr

def main(argv):
    sz = len(argv)
    if sz == 0 or sz > 1:
        print("Own argument require")
        return
    equation = parseArg(argv[0])
    print(equation)


if __name__ == "__main__":
    main(sys.argv[1:])
