# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    colors.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/08 16:00:34 by sbelondr          #+#    #+#              #
#    Updated: 2020/12/10 14:59:29 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    GRAY = '\033[97m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'

    def printFail(msg):
        print(bcolors.FAIL + msg + bcolors.END)

    def printFailDebug(msg):
        return (bcolors.FAIL + msg + bcolors.END + '\n')

    def printGreen(msg):
        print(bcolors.GREEN + msg + bcolors.END)

    def printGreenDebug(msg):
        return (bcolors.GREEN + msg + bcolors.END + '\n')

    def printBlue(msg):
        print(bcolors.BLUE + msg + bcolors.END)

    def printBlueDebug(msg):
        return (bcolors.BLUE + msg + bcolors.END + '\n')

    def printGray(msg):
        print(bcolors.GRAY + msg + bcolors.END)

    def printGrayDebug(msg):
        return (bcolors.GRAY + msg + bcolors.END + '\n')

    def printWarning(msg):
        print(bcolors.WARNING + msg + bcolors.END)

    def printWarningDebug(msg):
        return (bcolors.WARNING + msg + bcolors.END + '\n')
