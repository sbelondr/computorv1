# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    display.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/08 15:59:07 by sbelondr          #+#    #+#              #
#    Updated: 2020/06/29 02:13:32 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from colors import bcolors as msg

def displaySign(src, first):
    '''
    if it's the first and if the sign is + so we don't display the sign
    '''
    floatValue = repr(src)
    if floatValue[0] != '+' and floatValue[0] != '-':
            floatValue = '+' + floatValue
    if (first and floatValue[0] == '+'):
        floatValue = floatValue[1:]
    else:
        floatValue = floatValue[0] + ' ' + floatValue[1:]
    return floatValue

def displayReduceForm(equation, maxNb):
    first = True
    sz = len(equation)
    strFinal = 'Reduced form: '
    for x in equation:
        if x != 0 or (sz - 1 == 0 and first):
            tmp = displaySign(x, first)
            first = False
            strFinal += tmp + ' * X^' + str(sz - 1) + ' '
        sz -= 1
    if first == False:
        strFinal += '= 0'
        msg.printWarning(strFinal)
        msg.printBlue("Polynomial degree: " + str(maxNb))
