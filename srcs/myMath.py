# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    myMath.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/08 15:59:51 by sbelondr          #+#    #+#              #
#    Updated: 2021/01/21 17:02:06 by samuel           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math
#from __init__ import bcolors as msg
from colors import bcolors as msg

def checkNumber(nb):
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

def ft_division(a, b):
    if a == 0 or b == 0:
        return 0
    nb = a / b
    checkNumber(nb)
    return nb

def racineCarre(nb):
    nbr = nb**(0.5)
    checkNumber(nbr)
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
