#!/usr/local/bin/python
# -*- coding: utf-8 -*

##Iniciamos con la tarifa.
tarifa =30
##Ponemos nuestro incremento.
incremento = tarifa*1.0

##Validamos nuestro nombre.
nombre = raw_input('Ingrese nombre de usuario: ')
##Nuestra funcion para hacer los calculos.
def  validacion(nombre):

			##Usuario 1

	if (nombre == "Marco" or nombre == "Antonio" or nombre == "Jose" or nombre == "David" or nombre == "Emilio"):
		if nombre == 'Marco':
			passwd = raw_input('\nIngrese contraseña: ')
			if passwd == '1':
				print 'Bienvenido a la sesión'
				horast = input("\nIngrese las horas trabajadas: ")
				if horast <=40:
					sueldo = tarifa*horast
					print "La tarifa por ", horast, " horas trabajas es de $", sueldo, " dlls"
				elif horast>40:
					sueldo=tarifa*horast
					hextras = horast - 40
					gextra = hextras * incremento
					salario = sueldo + gextra
					print"El salario de la semana por trabajar ", hextras, " horas extras es de $ ", salario, " dlls"
				else:
					salario = 0
			else:
				print 'Contraseña incorrecta'

				##Usuario 2

		elif nombre == 'Antonio':
			passwd = raw_input('\nIngrese contraseña: ')
			if passwd == '1':
				print 'Bienvenido a la sesión'
				horast = input("\nIngrese las horas trabajadas: ")
				if horast <=40:
					sueldo = tarifa*horast
					print "La tarifa por ", horast, " horas trabajas es de $", sueldo, " dlls"
				elif horast>40:
					sueldo=tarifa*horast
					hextras = horast - 40
					gextra = hextras * incremento
					salario = sueldo + gextra
					print"El salario de la semana por trabajar ", hextras, " horas extras es de $ ", salario, " dlls"
				else:
					salario = 0
			else:
				print 'Contraseña incorrecta'

				##Usuario 3

		elif nombre == 'Jose':
			passwd = raw_input('\nIngrese contraseña: ')
			if passwd == '1':
				print 'Bienvenido a la sesión'
				horast = input("\nIngrese las horas trabajadas: ")
				if horast <=40:
					sueldo = tarifa*horast
					print "La tarifa por ", horast, " horas trabajas es de $", sueldo, " dlls"
				elif horast>40:
					sueldo=tarifa*horast
					hextras = horast - 40
					gextra = hextras * incremento
					salario = sueldo + gextra
					print"El salario de la semana por trabajar ", hextras, " horas extras es de $ ", salario, " dlls"
				else:
					salario = 0
			else:
				print 'Contraseña incorrecta'

				##Usuario 4

		elif nombre == 'David':
			passwd = raw_input('\nIngrese contraseña: ')
			if passwd == '1':
				print 'Bienvenido a la sesión'
				horast = input("\nIngrese las horas trabajadas: ")
				if horast <=40:
					sueldo = tarifa*horast
					print "La tarifa por ", horast, " horas trabajas es de $", sueldo, " dlls"
				elif horast>40:
					sueldo=tarifa*horast
					hextras = horast - 40
					gextra = hextras * incremento
					salario = sueldo + gextra
					print"El salario de la semana por trabajar ", hextras, " horas extras es de $ ", salario, " dlls"
				else:
					salario = 0
			else:
				print 'Contraseña incorrecta'

				##Usuario 5

		elif nombre == 'Emilio':
			passwd = raw_input('\nIngrese contraseña: ')
			if passwd == '1':
				print 'Bienvenido a la sesión'
				horast = input("\nIngrese las horas trabajadas: ")
				if horast <=40:
					sueldo = tarifa*horast
					print "La tarifa por ", horast, " horas trabajas es de $", sueldo, " dlls"
				elif horast>40:
					sueldo=tarifa*horast
					hextras = horast - 40
					gextra = hextras * incremento
					salario = sueldo + gextra
					print"El salario de la semana por trabajar ", hextras, " horas extras es de $ ", salario, " dlls"
				else:
					salario = 0
			else:

				##Si no pone nada en contrasena o no es valida

				print 'Contraseña incorrecta'
	else:

				##Si no pone usuario o es invalido.

		print "\nNombre de usuario incorrecto"

validacion(nombre)

