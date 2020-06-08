# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    myMath.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/08 15:59:51 by sbelondr          #+#    #+#              #
#    Updated: 2020/06/08 15:59:53 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from colors import bcolors

def ft_division(a, b):
    if a == 0 or b == 0:
        return 0
    return a / b

def racineCarre(nb):
    return (nb**(0.5))

def launchEquation(equation, delta, modeDebug):
    if modeDebug:
        print(bcolors.GRAY + "First equation: ( " + repr(-equation[1]) + " + " + repr(delta) + "^1/2 ) / ( 2 * " + repr(equation[0]) + " ):" + bcolors.END)
    result = ft_division(((-equation[1]) + racineCarre(delta)), (2 * equation[0]))
    print(bcolors.GREEN + repr(result) + bcolors.END)
    if modeDebug:
        print("\n" + bcolors.GRAY + "Second equation: ( " + repr(-equation[1]) + " - " + repr(delta) + "^1/2 ) / ( 2 * " + repr(equation[0]) + " ):" + bcolors.END)
    result = ft_division(((-equation[1]) - racineCarre(delta)), (2 * equation[0]))
    print(bcolors.GREEN + repr(result) + bcolors.END)