#!/usr/local/bin/python
# -*- coding: utf-8 -*-

##Diferentes

##list1, list2 = ["Verde","Rojo","Morado","Azul","Negro","Blanco","Rosa","Anaranjado"], ["Plateado","Guinda","Dorado","Menta","Gris","Lila","Amarillo","Crema"]

##Iguales

list1, list2 = ["Verde","Rojo","Morado","Azul","Negro","Blanco","Rosa","Anaranjado"], ["Verde","Rojo","Morado","Azul","Negro","Blanco","Rosa","Anaranjado"]
#Imprime el resultado de la comparación de ambas listas

print ("\nEl resultado: ", list1 == list2)

#Imprime los elementos de la lista 1
print "\nElementos de la lista 1:"
for ciclo in list1:
	print (ciclo)

#Imprime los elementos de la lista 2
print "\nElementos de la lista 2:"
for ciclo in list2:
	print (ciclo)
