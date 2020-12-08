#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

if __name__ == '__main__':
    x = float(input("Введите начальное количество километров - "))

    s = x
    for i in range(1, 7):
        x *= 1.1
        s += x
    print("Увеличивая дневную норму на 10% от предыдущего дня за 7 дней вы пробежите -", s, "км")
