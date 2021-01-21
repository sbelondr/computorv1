# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    computorv1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/01 13:03:11 by samuel            #+#    #+#              #
#    Updated: 2021/01/21 16:17:21 by samuel           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

from secondDegre import *
from colors import bcolors as msg
from myMath import ft_division, racineCarre
from display import displayReduceForm
from parlex import parseArg
from parser import parser
def firstDegre(dictio, modeDebug):
    '''
        First degre:
            (result - (n of X^0)) / n of X^1)
    '''
    msg.printBlue("The soluce is:")
    if modeDebug:
        msg.printGray("Equation: ( 0 - " + repr(dictio.get(0)) + " ) / "
                + repr(dictio.get(1)))
    msg.printGreen(repr(ft_division((0 - dictio.get(0)), dictio.get(1))))


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

def zeroDegre(dictio):
    if dictio.get(0) != 0:
        print('No solution')
    else:
        print("All real number can be a solution")

def main(argv):
    modeDebug = 0
    checkArg = verifArgument(argv)
    isGreater = 0
    if checkArg == 0:
        sys.exit()
    if checkArg == 2:
        modeDebug = 1
        dictioSort, dictio = parser(argv[1])
    else:
        dictioSort, dictio = parser(argv[0])
    maxNb = displayReduceForm(dictioSort, dictio)
    if maxNb > 2:
        msg.printFail("The polynomial degree is stricly greater than 2, "
                + "I can't solve.")
        sys.exit(-1)
    for x in range(3):
        if not x in dictio:
            dictio[x] = 0

    if dictio.get(2) == 0 and dictio.get(1) == 0:
        zeroDegre(dictio)
    elif dictio.get(2) == 0:
        firstDegre(dictio, modeDebug)
    else:
        polynominale2(dictio, modeDebug)

if __name__ == "__main__":
    main(sys.argv[1:])
