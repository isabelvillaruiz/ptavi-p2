#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2


if __name__ == "__main__":

    try:

        num1 = float(sys.argv[1])
        num2 = float(sys.argv[3])

    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = CalculadoraHija().plus(num1, num2)
    elif sys.argv[2] == "resta":
        result = CalculadoraHija().minus(num1, num2)
    elif sys.argv[2] == "multiplica":
        result = CalculadoraHija().multiply(num1, num2)
    elif sys.argv[2] == "divide":
        if num2 == 0.0:
            sys.exit('Division by zero is not allowed')
        else:
            result = CalculadoraHija().divide(num1, num2)
        else:
            sys.exit('This operation is not allowed ')
    print(result)
