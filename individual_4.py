#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

# Точность вычислений.
EPS = 1e-10

if __name__ == '__main__':
    x = float(input("Value of x? "))
    if x == 1:
        print("Illegal value of x", file=sys.stderr)
        exit(1)
    a = x
    S, n = a, 1

    # Найти сумму членов ряда.
    while math.fabs(a) > EPS:
        a *= 2 * x * n / (2 * n + 1) ** 2
        S += a
        n += 1
# Вывести значение функции.
print(f"Shi({x}) = {S}")