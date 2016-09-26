#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija


if __name__ == "__main__":
    calculadora = calcoohija.CalculadoraHija()
    fichero = open('fichero', 'r')
    lineas = fichero.readlines()

    #calculadora = calcoohija.CalculadoraHija()

    for linea in lineas:
        linea = linea.split(',')
        operacion = linea[0]
        operandos = linea[1:]
        lastop = operandos[0]

        for operando in operandos[1:]:
            if operacion == "suma":
                lastop = calculadora.plus(int(lastop), int(operando))
            elif operacion == "resta":
                lastop = calculadora.minus(int(lastop), int(operando))
            elif operacion == "multiplica":
                lastop = calculadora.multiply(int(lastop), int(operando))
            elif operacion == "divide":
                if (lastop or operando) == 0.0:
                    sys.exit('Division by zero is not allowed')
                else:
                    lastop = calculadora.divide(int(lastop), int(operando))
            else:
                sys.exit('This operation is not allowed ')
        print(lastop)
