# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    myMath.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/08 15:59:51 by sbelondr          #+#    #+#              #
#    Updated: 2020/06/30 03:37:17 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from colors import bcolors as msg

def ft_strToInt(src):
    if (src.isdigit()):
        return int(src)
    msg.printFail('Element "' + src + '" is not int')
    sys.exit(-1)

def ft_strToFloat(src):
    tmp = src.replace('.', '')
    if (tmp.isdigit()):
        return float(src)
    msg.printFail('Element "' + src + '" is not float or int')
    sys.exit(-1)

def ft_division(a, b):
    if a == 0 or b == 0:
        return 0
    return a / b

def racineCarre(nb):
    return (nb**(0.5))

def launchEquation(equation, delta, modeDebug):
    if modeDebug:
        msg.printGray("First equation: ( " + repr(-equation[1])
                + " + " + repr(delta) + "^1/2 ) / ( 2 * "
                + repr(equation[0]) + " ):")
    result = ft_division(((-equation[1]) + racineCarre(delta)), (2 * equation[0]))
    msg.printGreen(repr(result))
    if modeDebug:
        msg.printGray("Second equation: ( " + repr(-equation[1])
                + " - " + repr(delta) + "^1/2 ) / ( 2 * " + repr(equation[0])
                + " ):")
    result = ft_division(((-equation[1]) - racineCarre(delta)), (2 * equation[0]))
    msg.printGreen(repr(result))
