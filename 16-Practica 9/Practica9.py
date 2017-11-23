# -*- coding: utf-8 -*-
#Práctica 11

#Ejecutar la aplicación de serie de Fibonacci:
import time

def fibonacci(n):
	if n <=1: return n
	else:
		return fibonacci (n-2) + fibonacci (n-1)

#Controlar el tiempo de ejecución con la instrucción modulo Time y hacer un registro antes y otro después de su ejecución y calcular su diferencia.
def fun_time():
	ti = time.time()
	print fibonacci(20)
	tf = time.time()
	print tf-ti
fun_time()

#Agregar un decorador para que devuelva el resultado modificado en el formato que se requiera para el usuario.
def timeit(func):
	def timed(*args, **kw):
		ti = time.time()
		result = func(*args, **kw)
		tf = time.time()
		print('Time: {:.10f} sec'.format(tf-ti))
		return result
	return timed

@timeit
def prueba():
	return fibonacci(10)
print prueba()

#4.- Añadir el proceso PID y el consumo de RAM con el módulo resource.
@timeit
def prueba():
	return fibonacci(80)
print prueba()

#import resource
import time
import os

def timeit(func):
	def timed(*args, **kw):
		ts = time.time()
		pid = os.getppid()
		result = func(*args, **kw)
		te = time.time()
		maxmen = (resource.getrusaque(resource.RUSAGE_SELF).ru_maxrss)/1000
		info = (pid, func._name, te-ts, maxmen)
		print('PID: {} \nName: {} \nTime: {:.10f} sec\nRAM:{} MB'.format(*info))
	return timed