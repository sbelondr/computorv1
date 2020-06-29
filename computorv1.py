# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    computorv1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/01 13:03:11 by samuel            #+#    #+#              #
#    Updated: 2020/06/29 04:53:13 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

from secondDegre import *
from colors import bcolors as msg
from myMath import ft_division, racineCarre
from display import displayReduceForm
from parlex import parseArg

def firstDegre(equation, modeDebug):
    '''
        First degre:
            (result - (n of X^0)) / n of X^1)
    '''
    msg.printBlue("The soluce is:")
    if modeDebug:
        msg.printGray("Equation: ( 0 - " + repr(equation[2]) + " ) / "
                + repr(equation[1]))
    msg.printGreen(repr(ft_division((0 - equation[2]), equation[1])))


def errorMessage():
    msg.printFail("computorv1: error argument")
    msg.printWarning("usage: python computorv1 [-v] <equation>")

def verifArgument(argv):
    '''
        Check if debug flag is used (display equation and step for resolve equation)
    '''
    lenArgv = len(argv)
    if (lenArgv == 1):
        return 1
    elif (lenArgv == 2):
        if argv[0] == "-v":
            return 2
    errorMessage()
    return (0)

def zeroDegre(equation):
    if equation[2] != 0:
        print('No solution')
    else:
        print("All real number can be a solution")

def main(argv):
    modeDebug = 0
    checkArg = verifArgument(argv)
    if checkArg == 0:
        sys.exit()
    if checkArg == 2:
        modeDebug = 1
        equation, isGreater = parseArg(argv[1])
    else:
        equation, isGreater = parseArg(argv[0])
    displayReduceForm(equation, isGreater)
    # get 3 last line (x0 x1 and x2)
    equation = equation[-3:]
    if isGreater > 2:
        msg.printFail("The polynomial degree is stricly greater than 2, "
                + "I can't solve.")
        sys.exit()
    if equation[0] == 0 and equation[1] == 0:
        if equation[2] < 0:
            print("No solution")
        else:
            zeroDegre(equation)
    elif equation[0] == 0:
        firstDegre(equation, modeDebug)
    else:
        polynominale2(equation, modeDebug)

if __name__ == "__main__":
    main(sys.argv[1:])
