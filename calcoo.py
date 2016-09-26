#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora():

	def plus(self,operando1,operando2):
		return operando1+operando2
	def minus(self,operando1,operando2):
		return operando1-operando2

if __name__ == "__main__":

	
	try:
		operando1 = float(sys.argv[1])
		operando2 = float(sys.argv[3])

	except ValueError:

		sys.exit("Error: Non numerical parameters")

	if sys.argv[2] == "suma":
		result = Calculadora().plus(operando1,operando2)
	elif sys.argv[2] == "resta":
		result = Calculadora().minus(operando1,operando2)
	else:
		sys.exit('Operación sólo puede ser sumar o restar')


	print(result)

