#!/usr/bin/python

import sys

class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    GRAY = '\033[97m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'

def returnError():
    print(bcolors.FAIL + "Unexpected syntax" + bcolors.END)
    sys.exit()

def ft_division(a, b):
    if a == 0 or b == 0:
        return 0
    return a / b

def racineCarre(nb):
    return (nb**(0.5))

# Polynominale 2
def neutreEquation(equation, delta, modeDebug):
    print(bcolors.BLUE + "The solution is:" + bcolors.END)
    if (modeDebug):
        print(bcolors.GRAY + "Equation: -" + repr(equation[1]) + " / ( 2 * " + repr(equation[0]) + " )" + bcolors.END)
    result = ft_division(-equation[1], (2 * equation[0]))
    print(bcolors.GREEN + repr(result) + bcolors.END)

def positiveEquation(equation, delta, modeDebug):
    print(bcolors.BLUE + "Discriminant is strictly positive, the two solutions are:" + bcolors.END)
    if modeDebug:
        print(bcolors.GRAY + "First equation: ( " + repr(-equation[1]) + " + " + repr(delta) + "^1/2 ) / ( 2 * " + repr(equation[0]) + " ):" + bcolors.END)
    result = ft_division(((-equation[1]) + racineCarre(delta)), (2 * equation[0]))
    print(bcolors.GREEN + repr(result) + bcolors.END)
    if modeDebug:
        print("\n" + bcolors.GRAY + "Second equation: ( " + repr(-equation[1]) + " - " + repr(delta) + "^1/2 ) / ( 2 * " + repr(equation[0]) + " ):" + bcolors.END)
    result = ft_division(((-equation[1]) - racineCarre(delta)), (2 * equation[0]))
    print(bcolors.GREEN + repr(result) + bcolors.END)

def negativeEquation():
    print(bcolors.BLUE + "Discriminant is strictly negative, there is not solution." + bcolors.END)

def calcDelta(form, modeDebug):
    result = form[1]**2 - 4 * form[0] * form[2]
    if modeDebug:
        print(bcolors.GRAY + "Delta: " + repr(result) + bcolors.END)
    return result

def polynominale2(equation, modeDebug):
    print(bcolors.BLUE + "Polynomial degree: 2" + bcolors.END)
    delta = calcDelta(equation, modeDebug)
    if delta > 0:
        positiveEquation(equation, delta, modeDebug)
    elif delta == 0:
        neutreEquation(equation, delta, modeDebug)
    else:
        negativeEquation()

# Fin polynominale 2

# First degre
# ( result - (n of X^0) ) / n of X^1
def firstDegre(equation, modeDebug):
    print(bcolors.BLUE + "Polynomial degree: 1" + bcolors.END)
    print(bcolors.BLUE + "The soluce is:" + bcolors.END)
    if modeDebug:
        print(bcolors.GRAY + "Equation: ( 0 - " + repr(equation[2]) + " ) / " + repr(equation[1]) + bcolors.END)
    print(bcolors.GREEN + repr(ft_division((0 - equation[2]), equation[1])) + bcolors.END)

def determineMode(c):
    if (c == 'X'):
        return (0)
    elif c >= '0' and c <= '9':
        return (1)
    elif c == '+' or c == '-':
        return (2)
    elif c == '*':
        return (3)
    elif c == '^':
        return (4)
    elif c == '.':
        return 5
    elif c == '=':
        return (6)
    else:
        returnError()

# create group with separate by sign + or -
def parseBySign(lst):
    lenLst = len(lst)
    newLst = list()
    start = 0
    end = 1
    returnSign = 0

    while (end < lenLst):
        if lst[end][0] == 2:
            if returnSign == 1:
                if lst[start][1] == '+':
                    lst[start][1] = '-'
                else:
                    lst[start][1] = '+'
            newLst.append(lst[start: end])
            start = end
        elif lst[end][0] == 6:
            returnSign = 1
            newLst.append(lst[start: end])
            start = end
            if lst[start + 1][0] != 2:
                lst[start][0] = 2
                lst[start][1] = '+'
            else:
                start += 1
            end = start
        end += 1
    if (start != end):
        if returnSign == 1:
            if lst[start][1] == '+':
                lst[start][1] = '-'
            else:
                lst[start][1] = '+'
        newLst.append(lst[start:end])
    return newLst

def reduce(lst):
    line = len(lst)
    i = 0
    final = [0, 0, 0]
    while i < line:
        isX = 0
        nb = 1
        sign = '+'
        checkError = 0
        for x in lst[i]:
            if (checkError == 0 and x[0] == 2):
                sign = x[1]
            if (checkError != 0 and x[0] == 2):
                returnError()
            if (checkError == 1 and x[0] == 1):
                nb = float(x[1])
            if (checkError != 1 and x[0] == 1):
                returnError()
            if checkError != 2 and x[0] == 3:
                returnError()
            if (checkError == 3 and x[0] == 7):
                isX = int(x[1])
            if (checkError != 3 and x[0] == 7):
                returnError()
            checkError += 1
        if (checkError != 4):
            returnError()
        if (sign == '-'):
            nb *= -1
        final[isX] += nb
        i += 1
    final = [final[2], final[1], final[0]]
    return final

def parseArg(arg):
    i = 0
    row = -1
    lst = list()

    arg = arg.replace(' ', '')
    # add sign if is not here in first character
    if arg[0] != '+' and arg[0] != '-':
        arg = '+' + arg

    lenArg = len(arg)
    while i < lenArg:
        ret = determineMode(arg[i])
        # is ^
        if ret == 4:
            if lst[row][0] == 0 and (i + 1 < lenArg and determineMode(arg[i + 1]) == 1):
                lst[row][0] = 7
                lst[row][1] = arg[i + 1]
                i += 2
                while i < lenArg and (determineMode(arg[i]) == 1 or determineMode(arg[i]) == 5):
                    lst[row][1] = lst[row][1] + arg[i]
                    i += 1
            else:
                returnError()
        # is number
        elif ret == 1:
            row += 1
            lst.append([ret, arg[i]])
            i += 1
            while i < lenArg and (determineMode(arg[i]) == 1 or determineMode(arg[i]) == 5):
                lst[row][1] = lst[row][1] + arg[i]
                i += 1
        # other
        else:
            row += 1
            lst.append([ret, arg[i]])
            i += 1
    lst = parseBySign(lst)
    lst = reduce(lst)
    return lst

def displaySign(src, first):
    floatValue = repr(src)
    if floatValue[0] != '+' and floatValue[0] != '-':
            floatValue = '+' + floatValue
    if (first and floatValue[0] == '+'):
        floatValue = floatValue[1:]
    else:
        floatValue = floatValue[0] + ' ' + floatValue[1:]
    return floatValue

def displayReduceForm(equation):
    first = 1
    strFinal = "Reduced form: "
    if equation[0] != 0:
        tmp = displaySign(equation[0], first)
        strFinal += tmp + " * X^2 "
        first = 0
    if equation[1] != 0:
        tmp = displaySign(equation[1], first)
        strFinal += tmp + " * X^1 "
        first = 0
    tmp = displaySign(equation[2], first)
    strFinal += tmp + " * X^0 = 0"
    print(bcolors.WARNING + strFinal + bcolors.END)

def verifArgument(argv):
    lenArgv = len(argv)
    if (lenArgv == 1):
        return 1
    elif (lenArgv == 2):
        if argv[0] == "-v":
            return 2
    print(bcolors.FAIL + "computorv1: error argument" + bcolors.END)
    print(bcolors.WARNING + "./computor [-v] <equation>" + bcolors.END)
    return (0)

def main(argv):
    modeDebug = 0
    checkArg = verifArgument(argv)
    if checkArg == 0:
        sys.exit()
    if checkArg == 2:
        modeDebug = 1
        equation = parseArg(argv[1])
    else:
        equation = parseArg(argv[0])
    displayReduceForm(equation)
    if equation[0] == 0 and equation[1] == 0:
        print("Any number can be a solution")
    elif equation[0] == 0:
        firstDegre(equation, modeDebug)
    else:
        polynominale2(equation, modeDebug)

if __name__ == "__main__":
    main(sys.argv[1:])
