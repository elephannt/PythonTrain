#!/usr/local/bin/python
# -*- coding: utf-8 -*


##EJEMPLO1

## t0 = time.time()
## for i in xrange(1000000000000000):
## 	i+=5
## 	print time.time()-t0

## EJEMPLO2
## import cProfile, pstats, StringIO
## pr = cProfile.Profile()
## pr.enable()
## pr.disable()
## s = StringIO.StringIO()
## sortby = 'cumulative'
## ps = pstats.Stats(pr, stream = s).sort_stats(sortby)
## ps.print_stats()
## print s.getvalue()

## EJEMPLO3
## import profile
## pr = profile.Profile()
## for i in range(5):
## 	print pr.calibrate(10000)

##EJEMPLO4
## import cProfile
## import re
## cProfile.run('re.compile("foo|bar")')

##EJEMPLO5
## import pstats
## p = pstats.Stats('restats')
## p.strip_dirs().sort_stats(-1).print_stats()

##EJEMPLO6
##import time
##loop_count = 10000
##def method0():
##	var = "This is a short sentence"
##	for num in xrange(loop_count):
##		if "is" in var:
##			pass
##def method1():
##	var = "This is a short sentence"
##	for num in xrange(loop_count):
##		if var.find("is"):
##			pass
##t0= time.time()
##method0()
##print 'method0 :' + `time.time()-t0`
##t0 = time.time()
##method1()
##print 'method :' + `time.time()-t0`


##Implementacion de la practica en el examen.

import time

t0 = time.time()

##Iniciamos con la tarifa.
tarifa =30
##Ponemos nuestro incremento.
incremento = tarifa*1.0

##Validamos nuestro nombre.
print ("          +----------------------+")
print ("          |                      |")
nombre = raw_input('           Enter username: ')


##Nuestra funcion para hacer los calculos.
def  validacion(nombre):
	print ("          |                      |")
	print ("          +----------------------+")
			##Usuario 1

	if (nombre == "Marco" or nombre == "Antonio" or nombre == "Jose" or nombre == "David" or nombre == "Emilio"):
		if nombre == 'Marco':
			passwd = raw_input('\nEnter password: ')
			if passwd == '1':
				print ('Welcome back...',nombre)
				horast = input("\nHow many hours did you work?: ")
				if horast <=40:
					sueldo = tarifa*horast
					print ("Your hours are: ", horast, " Your payment is: $", sueldo, " Dlls")
				elif horast>40:
					sueldo=tarifa*horast
					hextras = horast - 40
					gextra = hextras * incremento
					salario = sueldo + gextra
					print"Your week hours are:  ", hextras, " including extra hours $ ", salario, " Dlls"
				else:
					salario = 0
			else:
				print 'Wrong password.'

				##Usuario 2

		elif nombre == 'Antonio':
			passwd = raw_input('\nEnter password: ')
			if passwd == '1':
				print 'Welcome back...',nombre
				horast = input("\nHow many hours did you work?: ")
				if horast <=40:
					sueldo = tarifa*horast
					print "Your hours are: ", horast, " Your payment is: $", sueldo, " Dlls"
				elif horast>40:
					sueldo=tarifa*horast
					hextras = horast - 40
					gextra = hextras * incremento
					salario = sueldo + gextra
					print"Your week hours are:  ", hextras, " including extra hours $ ", salario, " Dlls"
				else:
					salario = 0
			else:
				print 'Wrong password'

				##Usuario 3

		elif nombre == 'Jose':
			passwd = raw_input('\nEnter password: ')
			if passwd == '1':
				print 'Welcome back...',nombre
				horast = input("\nHow many hours did you work?: ")
				if horast <=40:
					sueldo = tarifa*horast
					print "Your hours are: ", horast, " Your payment is: $", sueldo, " Dlls"
				elif horast>40:
					sueldo=tarifa*horast
					hextras = horast - 40
					gextra = hextras * incremento
					salario = sueldo + gextra
					print"Your week hours are:  ", hextras, " including extra hours $ ", salario, " Dlls"
				else:
					salario = 0
			else:
				print 'Wrong password'

				##Usuario 4

		elif nombre == 'David':
			passwd = raw_input('\nEnter password: ')
			if passwd == '1':
				print 'Welcome back...',nombre
				horast = input("\nHow many hours did you work?: ")
				if horast <=40:
					sueldo = tarifa*horast
					print "Your hours are: ", horast, " Your payment is: $", sueldo, " Dlls"
				elif horast>40:
					sueldo=tarifa*horast
					hextras = horast - 40
					gextra = hextras * incremento
					salario = sueldo + gextra
					print"Your week hours are:  ", hextras, " including extra hours $ ", salario, " Dlls"
				else:
					salario = 0
			else:
				print 'Contraseña incorrecta'

				##Usuario 5

		elif nombre == 'Emilio':
			passwd = raw_input('\nEnter password: ')
			if passwd == '1':
				print 'Bienvenido a la sesión'
				horast = input("\nHow many hours did you work?: ")
				if horast <=40:
					sueldo = tarifa*horast
					print "Your hours are: ", horast, " Your payment is: $", sueldo, " Dlls"
				elif horast>40:
					sueldo=tarifa*horast
					hextras = horast - 40
					gextra = hextras * incremento
					salario = sueldo + gextra
					print"Your week hours are:  ", hextras, " including extra hours $ ", salario, " Dlls"
				else:
					salario = 0
			else:

				##Si no pone nada en contrasena o no es valida

				print 'Wrong password'
	else:

				##Si no pone usuario o es invalido.

		print "\nWrong username"

validacion(nombre)
print time.time()-t0

