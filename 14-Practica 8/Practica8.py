#!/usr/local/bin/python
# -*- coding: utf-8 -*
import os
import time
loop_count = 10000000
import random

def method0():
	var = "This is a short sentence"
	for num in xrange(loop_count):
		if "is" in var:
			pass
def method1():
	var = "This is a short sentence"
	for num in xrange(loop_count):
		if var.find("is"):
			pass

nombre=""
appat=""
apmat=""
dianac=""
anio=""
mes=""

def creartxt():
    archi=open('RFC.txt','w')
    archi.close()

def grabartxt():
    archi=open('RFC.txt','a')
    archi.write("       | Nombre: " + nombre)
    archi.write("\n       | Apellido paterno: " + appat)
    archi.write("\n       | Apellido materno: " + apmat)
    archi.write("\n       | Fecha de nacimiento: " + anio + "/" + mes + "/" + dianac)
    archi.write(" ")
    archi.write("\n       | Tu RFC es: ")
    archi.write(RFC)
    archi.close()

print "\n+------------------------------------------------------------------------+"
print "|        Ingresar los datos siguientes en mayusculas y sin acentos       |"
print "+------------------------------------------------------------------------+"

nombre = raw_input (" \n|        Nombre: ")
appat = raw_input ("|       | Apellido paterno: ")
apmat = raw_input ("|       | Apellido materno: ")
dianac = raw_input("|       | Dia nacimiento: ")
anio = raw_input ("|       | Año de nacimiento: ")
mes = raw_input ("|       | Numero de mes de nacimiento: ")


indice = 0
arregloApPa = []
posicionApPa=appat[0]
posicionApMa=apmat[0]
posicionNom= nombre[0]

t0 = time.time()
method0()
print '        | Generando RFC:     |' + `time.time()-t0`

t0 = time.time()
method1()

while indice < len(appat):
    letra = appat[indice]
    if letra == "A":
        arregloApPa.append("A")
    elif letra == "E":
        arregloApPa.append("E")
    elif letra == "I":
        arregloApPa.append("I")
    elif letra == "O":
        arregloApPa.append("O")
    elif letra == "U":
        arregloApPa.append("U")
    indice += 1

Aleatorios = ["YL1","ZU3","OI7","HV3","XE2","LM9","CZ2","PL9"]
posicion = random.randrange(7)

print("        | Tu RFC es:      |\n")
RFC = posicionApPa + arregloApPa[0] + posicionApMa + posicionNom + anio + mes + dianac + Aleatorios[posicion]
print (posicionApPa + arregloApPa[0] + posicionApMa + posicionNom + anio + mes + dianac + Aleatorios[posicion])
print ("|        | Tu RFC A SIDO GUARDADO                                        |")
print "+------------------------------------------------------------------------+"

print '|        | Generando RFC...:                                             |' + `time.time()-t0`
print "+------------------------------------------------------------------------+"

creartxt()
grabartxt()