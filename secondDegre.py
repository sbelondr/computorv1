# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    secondDegre.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/08 16:00:16 by sbelondr          #+#    #+#              #
#    Updated: 2020/06/08 16:00:27 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from colors import bcolors
from myMath import ft_division, racineCarre, launchEquation

# Polynominale 2
def neutreEquation(equation, delta, modeDebug):
    print(bcolors.BLUE + "Discriminant is 0. The solution is:" + bcolors.END)
    if (modeDebug):
        print(bcolors.GRAY + "Equation: -" + repr(equation[1]) + " / ( 2 * " + repr(equation[0]) + " )" + bcolors.END)
    result = ft_division(-equation[1], (2 * equation[0]))
    print(bcolors.GREEN + repr(result) + bcolors.END)

def positiveEquation(equation, delta, modeDebug):
    print(bcolors.BLUE + "Discriminant is strictly positive, the two solutions are:" + bcolors.END)
    launchEquation(equation, delta, modeDebug)

def negativeEquation(equation, delta, modeDebug):
    print(bcolors.BLUE + "Discriminant is strictly negative, the two solution are:" + bcolors.END)
    delta = -delta
    if modeDebug:
        print(bcolors.GRAY + repr(-equation[1])+ " / (2 * " + repr(equation[0])+ ") + i(" + repr(delta) + "^1/2 / (2 * " + repr(equation[0]) + ")) " + bcolors.END)
    print(bcolors.GREEN + repr(ft_division(-equation[1], (2 * equation[0]))) + " + i" + repr(ft_division(racineCarre(delta), (2 * equation[0]))) + bcolors.END)
    if modeDebug:
        print(bcolors.GRAY + repr(-equation[1])+ " / (2 * " + repr(equation[0])+ ") - i(" + repr(delta) + "^1/2 / (2 * " + repr(equation[0]) + ")) " + bcolors.END)
    print(bcolors.GREEN + repr(ft_division(-equation[1], (2 * equation[0]))) + " - i" + repr(ft_division(racineCarre(delta), (2 * equation[0]))) + bcolors.END)

def calcDelta(form, modeDebug):
    result = form[1]**2 - 4 * form[0] * form[2]
    if modeDebug:
        print(bcolors.GRAY + "Delta: " + repr(result) + bcolors.END)
    return result

def polynominale2(equation, modeDebug):
    delta = calcDelta(equation, modeDebug)
    if delta > 0:
        positiveEquation(equation, delta, modeDebug)
    elif delta == 0:
        neutreEquation(equation, delta, modeDebug)
    else:
        negativeEquation(equation, delta, modeDebug)
