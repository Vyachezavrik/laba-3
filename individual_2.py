#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = float(input("Введите число a - "))
    b = float(input("Введите число b - "))
    c = float(input("Введите число c - "))

    if abs(a) >= 4:
        print(a, "больше числа 4 по модулю")
    else:
        print(a, "по модулю меньше 4", file=sys.stderr)
    if abs(b) >= 4:
        print(b, "больше числа 4 по модулю")
    else:
        print(b, "по модулю меньше 4", file=sys.stderr)
    if abs(c) >= 4:
        print(c, "больше числа 4 по модулю")
    else:
        print(c, "по модулю меньше 4", file=sys.stderr)