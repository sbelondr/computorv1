# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    secondDegre.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/08 16:00:16 by sbelondr          #+#    #+#              #
#    Updated: 2021/01/21 16:57:23 by samuel           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from colors import bcolors as msg
from myMath import checkNumber, ft_division, racineCarre, launchEquation

# Polynominale 2
def neutreEquation(equation, delta, modeDebug):
    msg.printBlue("Discriminant is 0. The solution is:")
    if (modeDebug):
        msg.printGray("Equation: -" + repr(equation[1]) + " / ( 2 * "
                + repr(equation[0]) + " )")
    result = ft_division(-equation[1], (2 * equation[0]))
    msg.printGreen(repr(result))

def positiveEquation(equation, delta, modeDebug):
    msg.printBlue("Discriminant is strictly positive, the two solutions are:")
    launchEquation(equation, delta, modeDebug)

def negativeEquation(equation, delta, modeDebug):
    msg.printBlue("Discriminant is strictly negative, the two solution are:")
    delta = -delta
    if modeDebug:
        msg.printGray(repr(-equation[1])+ " / (2 * "
                + repr(equation[0])+ ") + i(" + repr(delta) + "^1/2 / (2 * "
                + repr(equation[0]) + ")) ")
    msg.printGreen(repr(ft_division(-equation[1], (2 * equation[0])))
            + " + i" + repr(ft_division(racineCarre(delta), (2 * equation[0]))))
    if modeDebug:
        msg.printGray(repr(-equation[1])+ " / (2 * " + repr(equation[0])
                + ") - i(" + repr(delta) + "^1/2 / (2 * " + repr(equation[0])
                + ")) ")
    msg.printGreen(repr(ft_division(-equation[1], (2 * equation[0])))
            + " - i" + repr(ft_division(racineCarre(delta), (2 * equation[0]))))

def calcDelta(form, modeDebug):
    result = form[1]**2 - 4 * form[0] * form[2]
    if modeDebug:
        msg.printGray("Delta: " + repr(result))
    return result

def polynominale2(dictio, modeDebug):
    equation = [dictio.get(2), dictio.get(1), dictio.get(0)]
    delta = calcDelta(equation, modeDebug)
    checkNumber(delta)
    if delta > 0:
        positiveEquation(equation, delta, modeDebug)
    elif delta == 0:
        neutreEquation(equation, delta, modeDebug)
    else:
        negativeEquation(equation, delta, modeDebug)
