# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parlex.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/08 15:59:23 by sbelondr          #+#    #+#              #
#    Updated: 2020/12/09 23:57:54 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from colors import bcolors as msg
from myMath import ft_strToInt, ft_strToFloat

def returnError():
    msg.printFail('Unexpected syntax')
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
    print(lst)
    final = [0, 0, 0]
    szFinal = 2
    i = 0
    lenLine = len(lst)
    while i < lenLine:
        degre = 0
        nb = 0
        x = lst[i]
        lenX = len(x)
        if lenX == 4:
            if x[0][0] == 2 and x[1][0] == 1 and x[2][0] == 3 and x[3][0] == 7:
              nb = ft_strToFloat(x[1][1])
              degre = ft_strToInt(x[3][1])
            else:
                returnError()
        elif lenX == 3:
            if x[0][0] == 2 and x[1][0] == 1 and x[2][0] == 7:
              nb = ft_strToFloat(x[1][1])
              degre = ft_strToInt(x[2][1])
            else:
                returnError()
        elif lenX == 2:
            if x[0][0] == 2 and x[1][0] == 1:
              nb = ft_strToFloat(x[1][1])
              degre = 0
            elif x[0][0] == 2 and x[1][0] == 7:
              nb = 1
              degre = ft_strToInt(x[1][1])
            else:
                returnError()
        else:
            returnError()
        if x[0][1] == '-':
            nb *= -1
        if degre > 2:
            while degre > szFinal:
                final.append(0)
                szFinal += 1
        final[degre] += nb

        i += 1
    final = final[::-1]
    return final

def ft_remove_whitespace(arg):
    arg = arg.replace(' ', '')
    arg = arg.replace('\n', '')
    arg = arg.replace('\r', '')
    return arg

def get_max(lst):
    final = 0
    cpy = lst[::-1]

    idx = 0
    for x in cpy:
        if x != 0:
            final = idx
        idx += 1
    return lst, final

def parseArg(arg):
    i = 0
    row = -1
    lst = list()

    arg = ft_remove_whitespace(arg)
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
        elif ret == 0 and (lenArg <= i + 1 or determineMode(arg[i + 1]) != 4):
            row += 1
            lst.append([7, '1'])
            i += 1
        # other
        else:
            row += 1
            lst.append([ret, arg[i]])
            i += 1
    lst = parseBySign(lst)
    lst = reduce(lst)
    lst, isGreater = get_max(lst)
    return lst, isGreater
