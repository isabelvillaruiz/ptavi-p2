#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class calculadora():
	def plus(self,num1,num2):
		return num1+num2

	def minus(self,num1,num2):
		return num1-num2

class CalculadoraHija(Calculadora): #Calculadora Hija hereda de Calculadora plus y minus

	def multiply(self,num1,num2):
		return num1 * num2	

	def divide(self,num1,num2):
		return num1 / num2


def Operaciones(num1,num2):

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

