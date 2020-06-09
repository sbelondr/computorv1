# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parlex.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/08 15:59:23 by sbelondr          #+#    #+#              #
#    Updated: 2020/06/09 10:25:23 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from colors import bcolors


def returnError():
    print(bcolors.FAIL + "Unexpected syntax" + bcolors.END)
    sys.exit()

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
    szFinal = 2
    isGreater = False

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
                if not x[1].isdigit():
                    print(bcolors.FAIL + x[1] + ' is not a int and computorv1 no manage the float degre' + bcolors.END)
                    sys.exit(-1)
                isX = int(x[1])
            if (checkError != 3 and x[0] == 7):
                returnError()

            checkError += 1

        if (checkError != 4):
            returnError()
        if (sign == '-'):
            nb *= -1
        if isX > 2:
            isGreater = True
            while isX > szFinal:
                final.append(0)
                szFinal += 1

        final[isX] += nb
        i += 1
    final = final[::-1]
    return final, isGreater

def parseArg(arg):
    i = 0
    row = -1
    lst = list()

    arg = arg.replace(' ', '')
    arg = arg.replace('\n', '')
    arg = arg.replace('\r', '')
    if (arg == ""):
        returnError()
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
    lst, isGreater = reduce(lst)
    return lst, isGreater
