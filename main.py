#!/usr/bin/python

import sys
# import array

def racineCarre(nb):
    return (nb**(0.5))

# Polynominale 2

def neutreEquation(equation, delta):
    print("The solution is:")
    result = (-equation[1]) / (2 * equation[0])
    print(result)
    pass

def positiveEquation(equation, delta):
    print("Discriminant is strictly positive, the two solutions are:")
    result = ((-equation[1]) + racineCarre(delta)) / (2 * equation[0])
    print(result)
    result = ((-equation[1]) - racineCarre(delta)) / (2 * equation[0])
    print(result)
    pass

def negativeEquation():
    print("Discriminant is strictly negative, there is not solution.")
    pass

def calcDelta(form):
    result = form[1]**2 - 4 * form[0] * form[2]
    return result

def polynominale2(equation):
    form = [float(equation[0][1]), float(equation[1][1]), float(equation[2][1])]
    if (equation[0][0] == "-"):
        form[0] *= -1
    if (equation[1][0] == "-"):
        form[1] *= -1
    if (equation[2][0] == "-"):
        form[2] *= -1
    delta = calcDelta(form)
    if delta > 0:
        positiveEquation(form, delta)
    elif delta == 0:
        neutreEquation(form, delta)
    else:
        negativeEquation()
    pass

# Fin polynominale 2

# later
def reduceForm():
    pass

def sortArrEquation(arr):
    a = []
    b = []
    c = []
    for x in arr:
        if x[3][2:] == "0":
            a = x
        elif x[3][2:] == "1":
            b = x
        elif x[3][2:] == "2":
            c = x
        else:
            print("error")
            sys.exit(1)
    return [c, b, a]


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
    arr = createArrEquation(arr)
    arr = sortArrEquation(arr)
    return arr

def main(argv):
    sz = len(argv)
    if sz == 0 or sz > 1:
        print("Own argument require")
        return
    equation = parseArg(argv[0])
    polynominale2(equation)



if __name__ == "__main__":
    main(sys.argv[1:])
