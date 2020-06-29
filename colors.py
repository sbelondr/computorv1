# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    colors.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/06/08 16:00:34 by sbelondr          #+#    #+#              #
#    Updated: 2020/06/29 02:25:16 by sbelondr         ###   ########.fr        #
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
        pass

    def printGreen(msg):
        print(bcolors.GREEN + msg + bcolors.END)
        pass

    def printBlue(msg):
        print(bcolors.BLUE + msg + bcolors.END)
        pass

    def printGray(msg):
        print(bcolors.GRAY + msg + bcolors.END)
        pass

    def printWarning(msg):
        print(bcolors.WARNING + msg + bcolors.END)
        pass
