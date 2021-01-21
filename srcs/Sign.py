# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Sign.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/21 11:12:16 by sbelondr          #+#    #+#              #
#    Updated: 2021/01/21 11:12:59 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from enum import Enum

class Symbol(Enum):
    WHITESPACE = 1
    NUMBER = 2
    X = 3
    SIGN = 4
    EQUAL = 5