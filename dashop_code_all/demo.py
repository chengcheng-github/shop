#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author JourWon
# @date 2021/3/3
# @file demo.py

x = 1000021
str_x = str(x)
if str_x[0] == '-':
    print(22)
if str_x[0] != str_x[-1]:
    print(33)
    for i in range(1,len(str_x)):
        num = -i-1
        print(str_x[i])
        print(str_x[num])
        if str_x[i] != str_x[num]:
            print(44)
else:
    print(11)



