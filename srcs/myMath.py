# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    myMath.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/08 15:59:51 by sbelondr          #+#    #+#              #
#    Updated: 2021/01/26 09:15:39 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math
from colors import bcolors as msg

def antiblockiersystem(nb):
    '''
        abs function
    '''
    return -nb if nb < 0 else nb

def checkNumber(nb):
    '''
        check number if it's inf or nan
    '''
    if nb == math.inf or nb == -math.inf or nb != nb:
        msg.printFail("This number is too large. I am not able to solve it.")
        sys.exit(-1)

def ft_strToInt(src):
    if (src.isdigit()):
        nb = int(src)
        checkNumber(nb)
        return nb
    msg.printFail('Element "' + src + '" is not int')
    sys.exit(-1)

def ft_strToFloat(src):
    tmp = src.replace('.', '', 1)
    if (tmp.find('.') == -1 and tmp.isdigit()):
        nb = float(src)
        checkNumber(nb)
        return nb
    msg.printFail('Element "' + src + '" is not float or int')
    sys.exit(-1)

def sqrt(nb, r):
    '''
        returns the square root of a number
    '''
    if r == 0:
        return 1
    neg = 1 if (nb < 0) else 0
    nb = antiblockiersystem(nb)
    result = nb
    r -= 1
    while (r > 0):
        result *= nb
        r -= 1
    return result if not neg else -result

def ft_division(a, b):
    '''
        check if a or b is zero and return division or error
    '''
    if b == 0:
        msg.printFail("Division by zero")
        sys.exit(-1)
    if a == 0:
        return 0
    nb = a / b
    checkNumber(nb)
    return nb

def racineCarre(nb):
    x = 3
    r = 10
    nb = antiblockiersystem(nb)
    while r > 0.00001:
        tmp = (x + (nb / x)) / 2
        r = antiblockiersystem(x - tmp)
        x = tmp

    nbr = x
    return nbr

def launchEquation(equation, delta, modeDebug):
    if modeDebug:
        msg.printGray("First equation: ( " + repr(-equation[1])
                + " + " + repr(delta) + "^1/2 ) / ( 2 * "
                + repr(equation[0]) + " ):")
    checkNumber(delta)
    result = ft_division(((-equation[1]) + racineCarre(delta)), (2 * equation[0]))
    msg.printGreen(repr(result))
    if modeDebug:
        msg.printGray("Second equation: ( " + repr(-equation[1])
                + " - " + repr(delta) + "^1/2 ) / ( 2 * " + repr(equation[0])
                + " ):")
    result = ft_division(((-equation[1]) - racineCarre(delta)), (2 * equation[0]))
    msg.printGreen(repr(result))
