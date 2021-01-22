# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parser.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/21 09:53:15 by sbelondr          #+#    #+#              #
#    Updated: 2021/01/22 10:34:39 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from lexer import lexer
from Sign import Symbol
from myMath import ft_strToFloat, ft_strToInt
from colors import bcolors as msg

def errorMessage():
    msg.printFail('Unexpected syntax')
    sys.exit()

def isWhitespace(arg, i, sz):
    while i < sz and (arg[i] == ' ' \
            or arg[i] == '\t' or arg[i] == '\r' or arg[i] == '\n'):
        i += 1
    return i

def isNumber(arg, i, sz, isFloat):
    nbStr = ''
    while i < sz and ((arg[i] >= '0' and arg[i] <= '9') or arg[i] == '.'):
        nbStr = nbStr + arg[i]
        i += 1
    if isFloat:
        return i, [Symbol.NUMBER, ft_strToFloat(nbStr)] if nbStr != '' else 0
    return i, [Symbol.NUMBER, ft_strToInt(nbStr)] if nbStr != '' else 0

def conditionX(arg, i, sz, sign):
    if arg[i] == 'X':
        i = isWhitespace(arg, i + 1, sz)
        if i < sz and arg[i] == '^':
            i = isWhitespace(arg, i + 1, sz)
            if i < sz:
                i, nb = isNumber(arg, i, sz, False)
                if nb != 0:
                    return i, [Symbol.X, nb]
        elif i == sz or (i <= sz and (arg[i] == '=' \
                or arg[i] == '-' or arg[i] == '+')):
            return i, [Symbol.X, [Symbol.NUMBER, 1]]
        errorMessage()
    if sign == 1:
        errorMessage()
    return i, 0

def isX(arg, i, sz):
    if arg[i] == '*':
        i = isWhitespace(arg, i + 1, sz)
        if i >= sz:
            errorMessage()
        return conditionX(arg, i, sz, 1)
    else:
        return conditionX(arg, i, sz, 0)
    return i, 0

def isSign(c, i, sz):
    if i < sz and (c == '-' or c == '+'):
        return i + 1, [Symbol.SIGN, c]
    return i, 0

def isEqual(c, i, sz):
    if i < sz and (c == '='):
        return i + 1, [Symbol.EQUAL, c]
    return i, 0

def parser(arg):
    lst = list()
    sz = len(arg)
    i = 0
    checkExist = 0
    while (i < sz):
        checkExist = i
        i = isWhitespace(arg, i, sz)
        i, line = isNumber(arg, i, sz, True)
        if line != 0:
            lst.append(line)
        if i >= sz:
            break
        i, line = isX(arg, i, sz)
        if line != 0:
            lst.append(line)
        if i >= sz:
            break
        i, line = isSign(arg[i], i, sz)
        if line != 0:
            lst.append(line)
        if i >= sz:
            break
        i, line = isEqual(arg[i], i, sz)
        if line != 0:
            lst.append(line)
        if checkExist == i:
            errorMessage()
    return lexer(lst)
