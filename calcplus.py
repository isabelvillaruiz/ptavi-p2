#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class calculadora():
	def plus(self,num1,num2):
		return num1+num2

	def minus(self,num1,num2):
		return num1-num2


class CalculadoraHija(calculadora): #Calculadora Hija hereda de Calculadora plus y minus


	def multiply(self,num1,num2):
		return num1 * num2	

	def divide(self,num1,num2):
		return num1 / num2



def Operaciones(num1,num2):

	if operacion == "suma":
		result = calculadora().plus(operando1,operando2)
	elif operacion == "resta":
		result = calculadora().minus(operando1,operando2)
	elif operacion == "multiplica":

		result =  calculadora().multiply(operando1,operando2)

	elif operacion == "divide" :
		if operando2 == 0:
			sys.exit('Division by zero is not allowed')
		else:

			result = calculadora().divide(operando1,operando2)
	else:
		sys.exit('This operation is not allowed ')


def leerfichero ( fichero , operacion ):
	
	fichero = open('fichero.txt','r')
	fichero.readline() 
	
	print(fichero.split(','))




