#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class calculadora():
	def plus(num1,num2):
		return num1+num2
	def minus(num1,num2):
		return num1-num2

if __name__ == "__main__":

	
	try:
		operando1 = float(sys.argv[1])
		operando2 = float(sys.argv[3])
	except ValueError:
		sys.exit("Error: Non numerical parameters")

	if sys.argv[2] == "suma":
		result = calculadora.plus(operando1,operando2)
	elif sys.argv[2] == "resta":
		result = calculadora.minus(operando1,operando2)
	else:
		sys.exit('Operación sólo puede ser sumar o restar')


	print(result)

