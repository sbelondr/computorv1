# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    myMath.test.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/10 00:13:04 by sbelondr          #+#    #+#              #
#    Updated: 2020/12/10 15:26:17 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import unittest
import io

import os
import sys

p = os.path.abspath('../srcs')
if p not in sys.path:
    sys.path.append(p)
from __init__ import *

def init_output():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    return capturedOutput

def reset_output():
    sys.stdout = sys.__stdout__

class TestDivisionMethods(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(ft_division(10, 1) == 10)
        self.assertTrue(ft_division(-10, 1) == -10)
        self.assertTrue(ft_division(10, 5) == 2)
        self.assertTrue(ft_division(-10, -10) == 1)

    def test_zero(self):
        self.assertTrue(ft_division(0, 3) == 0)
        self.assertTrue(ft_division(0.0, 3) == 0)
        self.assertTrue(ft_division(10, 0) == 0)
        self.assertTrue(ft_division(10, 0.0) == 0)
        self.assertTrue(ft_division(0, 0) == 0)
        self.assertTrue(ft_division(0, -12) == 0)

#        # check that s.split fails when the separator is not a string
 #       with self.assertRaises(TypeError):
  #          s.split(2)

class TestStrToInt(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(ft_strToInt("123") == 123)

    def test_float(self):
        capturedOutput = init_output()
        with self.assertRaises(SystemExit) as cm:
            ft_strToInt("1.123")
        reset_output();
        self.assertEqual(cm.exception.code, -1)
        self.assertEqual(capturedOutput.getvalue(),
                msg.printFailDebug('Element "1.123" is not int'))

    def test_char(self):
        capturedOutput = init_output()
        with self.assertRaises(SystemExit) as cm:
            ft_strToInt("a")
        reset_output();
        self.assertEqual(cm.exception.code, -1)
        self.assertEqual(capturedOutput.getvalue(),
                msg.printFailDebug('Element "a" is not int'))

if __name__ == '__main__':
    unittest.main(exit=False)
