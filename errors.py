#!/usr/bin/env python3.3
## errors.py for  in /home/tetard/EPITECH_Y2/maths/202unsold
##
## Made by benjamin girard
## Login   <tetard@epitech.net>
##
## Started on  Mon Feb 27 17:03:27 2017 benjamin girard
## Last update Mon Feb 27 17:09:01 2017 benjamin girard
##

import sys

def check_int(string):
    try:
        i = int(string)
        return i
    except ValueError:
        return None

def check_err():
    arg_list = []
    if (len(sys.argv) - 1) == 2:
        for arg in sys.argv[1:3]:
            arg_list.append(check_int(arg))
        for arg in arg_list:
            if arg == None or arg < 50:
                return None
        return arg_list
    return None
