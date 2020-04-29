#!/usr/bin/python

import sys
# import array

def racineCarre(nb):
    return (nb**(0.5))

# Polynominale 2

def neutreEquation(equation, delta):
    pass

def positiveEquation(equation, delta):
    pass

def negativeEquation():
    
    pass

def calcPoly2(form):
    for x in form:
        print(x)
    result = form[1]**2 - 4 * form[0] * form[2]
    print(result)
    return result

def polynominale2(equation):
    form = [float(equation[0][1]), float(equation[1][1]), float(equation[2][1])]
    if (equation[0][0] == "-"):
        form[0] *= -1
    if (equation[1][0] == "-"):
        form[1] *= -1
    if (equation[2][0] == "-"):
        form[2] *= -1
    delta = calcPoly2(form)
    if delta > 0:
        positiveEquation(equation, delta)
    elif delta == 0:
        neutreEquation(equation, delta)
    else
        negativeEquation()
    pass

# Fin polynominale 2

# later
def reduceForm():
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
    polynominale2(equation)



if __name__ == "__main__":
    main(sys.argv[1:])
