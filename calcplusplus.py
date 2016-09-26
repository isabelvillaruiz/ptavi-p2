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
			ultimooperando = operandos[0]
	

			for operando in operandos[1:]:
			
				if operacion == "suma":
					ultimooperando = calculadora.plus(int(ultimooperando),int(operando))
				elif operacion == "resta":
					ultimooperando = calculadora.minus(int(ultimooperando),int(operando))
				elif operacion == "multiplica":
			
					ultimooperando =  calculadora.multiply(int(ultimooperando),int(operando))
	
				elif operacion == "divide" :
					if (ultimooperando or operando) == 0.0:
						sys.exit('Division by zero is not allowed')
					else:
						ultimooperando = calculadora.divide(int(ultimooperando),int(operando))
				else:
					sys.exit('This operation is not allowed ')
	
			print(ultimooperando)

	




