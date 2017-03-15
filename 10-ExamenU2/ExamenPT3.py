#!/usr/local/bin/python
# -*- coding: utf-8 -*-

pago = 28
incremento = pago*0.03
horast = input("Ingrese las horas trabajadas: ")
def condicion():
	if horast <= 30:
		tarifah = pago * horast
		print "El salario es de: $",tarifah," dlls"
	else:
		salario = horast*(pago+(incremento))#pago*0.03))
		print "El salario es de: $", salario," dlls"
condicion()