# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    display.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/08 15:59:07 by sbelondr          #+#    #+#              #
#    Updated: 2021/01/22 10:36:17 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from colors import bcolors as msg

def formatEquation(key, value, first):
    strValue = repr(value) if value >= 0 else repr(-value)
    sign = ' ' if not first else ''
    if value < 0:
        sign += '- '
    elif not first:
        sign += '+ '
    return sign + strValue + ' * X^' + str(key)

def displayReduceForm(dictioSort, dictio):
    maxNb = 0
    first = True
    sz = len(dictioSort) - 1
    strFinal = 'Reduced form: '
    for key in dictioSort:
        value = dictio.get(key)
        if value != 0:
            strFinal +=  formatEquation(key, dictio.get(key), first)
            maxNb = key
            if first:
                first = not first
    if first == False:
        strFinal += ' = 0'
        msg.printWarning(strFinal)
        msg.printBlue("Polynomial degree: " + str(maxNb))
    else:
        msg.printBlue("Polynomial degree: " + str(maxNb))
        msg.printWarning("Reduced form: 0 = 0")
        print("All real number can be a solution")
        sys.exit(-1)
    return maxNb
