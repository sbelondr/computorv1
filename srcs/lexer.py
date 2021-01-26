# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    lexer.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/21 11:13:37 by sbelondr          #+#    #+#              #
#    Updated: 2021/01/26 09:54:59 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Sign import Symbol
from colors import bcolors as msg
import sys

def errorMessage():
    msg.printFail('Unexpected syntax')
    sys.exit()


def ftX(lst, i, sz):
    i += 1
    if i < sz:
        if lst[i][0] != Symbol.SIGN and lst[i][0] != Symbol.EQUAL:
            errorMessage()
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
        errorMessage()
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
        errorMessage()
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
    if len(lst) <= 0 or lst[len(lst) - 1][0] == Symbol.EQUAL:
            errorMessage()
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
                errorMessage()
            reverseSign = True
        i += 1
    dictSort = sorted(dictio)
    return dictSort, dictio
