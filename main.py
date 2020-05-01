#!/usr/bin/python

import sys

def returnError():
    print("Unexpected syntax")
    sys.exit()

def ft_division(a, b):
    if a == 0 or b == 0:
        return 0
    return a / b

def racineCarre(nb):
    return (nb**(0.5))

# Polynominale 2
def neutreEquation(equation, delta):
    print("The solution is:")
    result = ft_division(-equation[1], (2 * equation[0]))
    print(result)

def positiveEquation(equation, delta):
    print("Discriminant is strictly positive, the two solutions are:")
    result = ft_division(((-equation[1]) + racineCarre(delta)), (2 * equation[0]))
    print(result)
    result = ft_division(((-equation[1]) - racineCarre(delta)), (2 * equation[0]))
    print(result)

def negativeEquation():
    print("Discriminant is strictly negative, there is not solution.")

def calcDelta(form):
    result = form[1]**2 - 4 * form[0] * form[2]
    return result

def polynominale2(equation):
    print("Polynomial degree: 2")
    delta = calcDelta(equation)
    if delta > 0:
        positiveEquation(equation, delta)
    elif delta == 0:
        neutreEquation(equation, delta)
    else:
        negativeEquation()

# Fin polynominale 2

# First degre
# ( result - (n of X^0) ) / n of X^1
def firstDegre(equation):
    print("Polynomial degree: 1")
    print("The soluce is:")
    print(ft_division((0 - equation[2]), equation[1]))

def determineMode(c):
    if (c == 'X'):
        return (0)
    elif c >= '0' and c <= '9':
        return (1)
    elif c == '+' or c == '-':
        return (2)
    elif c == '*' or c == '/':
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
            if lst[row][0] == 0 and determineMode(arg[i + 1]) == 1:
                lst[row][0] = 7
                lst[row][1] = arg[i + 1]
                i += 2
                while i < lenArg and (determineMode(arg[i]) == 1 or determineMode(arg[i]) == 5):
                    lst[row][1] = lst[row][1] + arg[i]
                    i += 1
            else:
                print("Unspected syntax")
                sys.exit()
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
    print(strFinal)

def main(argv):
    sz = len(argv)
    if sz == 0 or sz > 1:
        print("Own argument require")
        return
    equation = parseArg(argv[0])
    displayReduceForm(equation)
    if equation[0] == 0 and equation[1] == 0:
        print("Any number can be a solution")
    elif equation[0] == 0:
        firstDegre(equation)
    else:
        polynominale2(equation)

if __name__ == "__main__":
    main(sys.argv[1:])
