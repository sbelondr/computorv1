# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    lexer.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/21 11:13:37 by sbelondr          #+#    #+#              #
#    Updated: 2021/01/21 12:57:35 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Sign import Symbol
import sys

def errorMessageBis():
    print("Not work")
    sys.exit(-1)

def ftX(lst, i, sz):
    i += 1
    if i < sz:
        if lst[i][0] != Symbol.SIGN and lst[i][0] != Symbol.EQUAL:
            errorMessageBis()
    #if (lst[i - 1][1] != 0):
    return lst[i - 1][1][1]

def ftNumber(lst, i, sz, reverseSign, neg):
    if reverseSign:
        neg = not neg
    x = 0
    nb = lst[i][1] if not neg else -lst[i][1]
    i += 1
    if i < sz and lst[i][0] == Symbol.X:
        x = ftX(lst, i, sz)
        i += 1
    elif i < sz and lst[i][0] == Symbol.NUMBER:
        errorMessageBis()
    i -= 1
    return i, nb, x

def ftSign(lst, i, sz, reverseSign):
    neg = True if lst[i][1] == '-' else False
    i += 1
    nb = 0
    if i < sz and lst[i][0] == Symbol.NUMBER:
        i, nb, x = ftNumber(lst, i, sz, reverseSign, neg)
    elif i < sz and lst[i][0] == Symbol.X:
        x = ftX(lst, i, sz)
        if reverseSign:
            neg = not neg
        nb = 1 if not neg else -1
    else:
        errorMessageBis()
    return i, nb, x

def addValue(dictio, x, nb):
    if x in dictio:
        dictio[x] = dictio[x] + nb
    else:
        dictio[x] = nb
    return dictio


def lexer(lst):
    dictio = dict()
    reverseSign = False
    sz = len(lst)
    i = 0
    while i < sz:
        if lst[i][0] == Symbol.SIGN:
            i, nb, x = ftSign(lst, i, sz, reverseSign)
            dictio = addValue(dictio, x, nb)
        elif lst[i][0] == Symbol.NUMBER:
            i, nb, x = ftNumber(lst, i, sz, reverseSign, False)
            dictio = addValue(dictio, x, nb)
        elif lst[i][0] == Symbol.X:
            x = ftX(lst, i, sz)
            nb = 1 if not reverseSign else -1
            dictio = addValue(dictio, x, nb)
        elif lst[i][0] == Symbol.EQUAL:
            if reverseSign:
                errorMessageBis()
            reverseSign = True
        i += 1
    dictSort = sorted(dictio)
    for key in dictSort:
        print(str(key) + " - " +str(dictio.get(key)))
    return 0
