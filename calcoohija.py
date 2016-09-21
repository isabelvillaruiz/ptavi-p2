#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class calculadora():
	def plus(self,num1,num2):
		return num1+num2

	def minus(self,num1,num2):
		return num1-num2

	def multiply(self,num1,num2):
		return num1 * num2	

	def divide(self,num1,num2):
		return num1 / num2


if __name__ == "__main__":

	
	try:
		operando1 = float(sys.argv[1])
		operando2 = float(sys.argv[3])
	except ValueError:
		sys.exit("Error: Non numerical parameters")

	if sys.argv[2] == "suma":
		result = calculadora().plus(operando1,operando2)
	elif sys.argv[2] == "resta":
		result = calculadora().minus(operando1,operando2)
	elif sys.argv[2] == "multiplica":
		result =  calculadora().multiply(operando1,operando2)
	elif sys.argv[2] == "divide" :
		if operando2 == 0:
			sys.exit('Division by zero is not allowed')
		else:
			result = calculadora().divide(operando1,operando2)
	else:
		sys.exit('This operation is not allowed ')


print(result)
