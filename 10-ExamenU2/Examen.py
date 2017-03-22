#!/usr/local/bin/python
# -*- coding: utf-8 -*

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

