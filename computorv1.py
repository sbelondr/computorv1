# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    computorv1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/01 13:03:11 by samuel            #+#    #+#              #
#    Updated: 2020/06/28 04:09:41 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

from secondDegre import *
from colors import bcolors
from myMath import ft_division, racineCarre
from display import displayReduceForm
from parlex import parseArg

def firstDegre(equation, modeDebug):
    '''
        First degre:
            (result - (n of X^0)) / n of X^1)
    '''
    print(bcolors.BLUE + "The soluce is:" + bcolors.END)
    if modeDebug:
        print(bcolors.GRAY + "Equation: ( 0 - " + repr(equation[2]) + " ) / " + repr(equation[1]) + bcolors.END)
    print(bcolors.GREEN + repr(ft_division((0 - equation[2]), equation[1])) + bcolors.END)


def errorMessage():
    print(bcolors.FAIL + "computorv1: error argument" + bcolors.END)
    print(bcolors.WARNING + "./computor [-v] <equation>" + bcolors.END)

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
        print(bcolors.FAIL + "The polynomial degree is stricly greater than 2, I can't solve." + bcolors.END)
        sys.exit()
    if equation[0] == 0 and equation[1] == 0:
        if equation[2] < 0:
            print("No solution")
        else:
            print("All real number can be a solution")
    elif equation[0] == 0:
        firstDegre(equation, modeDebug)
    else:
        polynominale2(equation, modeDebug)

if __name__ == "__main__":
    main(sys.argv[1:])
