# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    display.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/08 15:59:07 by sbelondr          #+#    #+#              #
#    Updated: 2020/06/08 16:09:17 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from colors import bcolors

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

def displayReduceForm(equation):
    first = True
    sz = len(equation)
    strFinal = 'Reduced form: '
    polynominal = 0

    for x in equation:
        if x != 0:
            tmp = displaySign(x, first)
            first = False
            strFinal += tmp + ' * X^' + str(sz - 1) + ' '
            if sz - 1 > polynominal:
                polynominal = sz - 1
        sz -= 1
    if first == False:
        strFinal += '= 0'
        print(bcolors.WARNING + strFinal + bcolors.END)
        print(bcolors.BLUE + "Polynomial degree: " + str(polynominal) + bcolors.END)
