#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import calcoohija
import csv


if __name__ == "__main__":

    fichero = sys.argv[1]
    with open(fichero) as operaciones:

        fichero = csv.reader(operaciones)
        calculadora = calcoohija.CalculadoraHija()

        for linea in fichero:
            operacion = linea[0]
            operandos = linea[1:]
            lastop = operandos[0]
            for ope in operandos[1:]:
                if operacion == "suma":
                    lastop = calculadora.plus(int(lastop), int(ope))
                    elif operacion == "resta":

                        lastop = calculadora.minus(int(lastop), int(ope))

                    elif operacion == "multiplica":

                        lastop = calculadora.multiply(int(lastop), int(ope))
                    elif operacion == "divide":

                        if (lastop or ope) == 0.0:
                            sys.exit('Division by zero is not allowed')
                        else:

                            lastop = calculadora.divide(int(lastop), int(ope))
                        else:
                            sys.exit('This operation is not allowed ')
                print(lastop)
