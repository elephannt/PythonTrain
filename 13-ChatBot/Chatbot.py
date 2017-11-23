#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import random, threading, time , sys , os
from time import sleep

##Builder
##Es usado para permitir la creacion de una variedad de objetos complejos desde un objeto fuente (Producto),
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

## Abstract Factory // Factory Method
##El patrón Abstract Factory nos permite crear, mediante una interfaz, conjuntos o familias de objetos
##(denominados productos) que dependen mutuamuente y todo esto sin especificar cual es el objeto concreto.

class MiThread(threading.Thread):
    def __init__(self,evento):
        threading.Thread.__init__(self)
        self.evento=evento
    def run(self):
        print (self.getName(),"En espera del evento")
        self.evento.wait()
        print (self.getName(),"Fin del evento")
evento = threading.Event()

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']

##Patron Prototype
##tiene como finalidad crear nuevos objetos duplicándolos, clonando una instancia creada previamente.

random_greeting = random.choice(greetings)

question = ['How are you?','How are you doing?']
responses = ['Okay',"I'm fine"]
random_response = random.choice(responses)

## Singleton
##Es un patrón de diseño diseñado para restringir
## la creación de objetos pertenecientes a una clase o el valor de un tipo a un5 único objeto.
os.system('clear')
print ("\n     +-------------------------------------------------------------------------------------------------+")
print ("     |					         LOGIN SCREEN					       |")
print ("     +-------------------------------------------------------------------------------------------------+")
print "     | Current IP address: ",s.getsockname()[0]
print ("\n     +-------------------------------------------------------------------------------------------------+")
s.close()
user = raw_input("     | Please enter your username: ")
password = raw_input("     | Please enter your password: ")
acct = raw_input("     | Please enter your account number: ")

print ("     | Going to verify information, please wait...")
print("\n")
for i in range(21):
    						sys.stdout.write('\r')
    						sys.stdout.write("					[%-20s] %d%%" % ('='*i, 5*i))
    						sys.stdout.flush()
    						sleep(0.25) ##0.25
time.sleep(3)  # Es posible cambiar el numero
evento.set()
if user == "m" and password == "m" and acct == "123":
	os.system('clear')
	s = """
                      _-.                     .-_
                  _..-'(                       )`-.._
               ./'. '||\\.       (\_/)       .//||` .`\.
            ./'.|'.'||||\\|..    )*.*(    ..|//||||`.`|.`\.
        ./'..|'.|| |||||\```````  "  '''''''/||||| ||.`|..`\.
      ./'.||'.|||| ||||||||||||.     .|||||||||||| ||||.`||.`\.
     /'|||'.|||||| ||||||||||||{     }|||||||||||| ||||||.`|||`
    '.|||'.||||||| ||||||||||||{     }|||||||||||| |||||||.`|||.`
   '.||| ||||||||| |/'   ``\||/`     '\||/''   `\| ||||||||| |||.`
   |/' \./'     `\./          |/\   /\|          \./'     `\./ `\|
   V    V         V          }' `\ /' `{          V         V    V
   `    `         `               U               '         '

"""
	print (s)
	print ("     	Loading program, please wait...\n")
	print("")
	for i in range(21):
    						sys.stdout.write('\r')
    						sys.stdout.write("     	[%-20s] %d%%" % ('='*i, 5*i))
    						sys.stdout.flush()
    						sleep(0.25)
	while True:
		os.system('clear')
		print ("\n     +-------------------------------------------------------------------------------------------------+")
		print ("     |					         WELCOME BACK					       |")
		print ("     +-------------------------------------------------------------------------------------------------+")
		print ("     | CCON: Cannot connect on network.						                       |")
		print ("     | ASO: All services out.								 	       |")
		print ("     | ACO: All channels out.								  	       |")
		print ("     | Billing: Billing question.						 		       |")
		print ("     +-------------------------------------------------------------------------------------------------+")

		userInput = raw_input("     | Username >>> ")
		if userInput in greetings:
			print(random_greeting)
		elif userInput in question:
			print(random_response)

		elif userInput == "CCON":
			print ("     +-------------------------------------------------------------------------------------------------+")
			print ("     | BestChatBOT: Do you have any lights on the BHR?					               |")
			print ("     +-------------------------------------------------------------------------------------------------+")
			userInput1 = raw_input("     | Username >>> ")
			if userInput1 == "No" or userInput1 == "no":
				print ("     +-------------------------------------------------------------------------------------------------+")
				print ("     | BestChatBOT: Make sure that the BHR its connected to the poweroutlet. Do you have lights?       |")
				print ("     +-------------------------------------------------------------------------------------------------+")
				userInput2 = raw_input("     | Username >>> ")
				if userInput2 == "Yes" or userInput2 == "yes":
					print ("     +-------------------------------------------------------------------------------------------------+")
					print ("     | BestChatBot: Do you have internet connection					               |")
					print ("     +-------------------------------------------------------------------------------------------------+")
					userInput3 = raw_input("     | Username >>> ")
					if userInput3 == "Yes" or userInput3 == "yes":
						print ("     +-------------------------------------------------------------------------------------------------+")
						print ("     | BestChatBot: Its great to hear that we got your internet back, have a good day!			  	   |")
						print ("     +-------------------------------------------------------------------------------------------------+")
						break
					elif userInput3 == "No" or userInput3 == "no":
						print ("     +-------------------------------------------------------------------------------------------------+")
						print ("     | BestChatBot: We are going to Break the DHCP lease, please wait..				       |")
						print ("\n")
						for i in range(21):
    							sys.stdout.write('\r')
    							sys.stdout.write("					[%-20s] %d%%" % ('='*i, 5*i))
    							sys.stdout.flush()
    							sleep(0.25)
						print ("\n")
						print ("\n     +-------------------------------------------------------------------------------------------------+")
						print ("     +-------------------------------------------------------------------------------------------------+")
						print ("     | BestChatBot: Do you have internet connection now?		 		               |")
						print ("     +-------------------------------------------------------------------------------------------------+")
						userInput4 = raw_input("     | Username >>> ")
						if userInput4 == "Yes" or userInput4 == "yes":
							print ("     +-------------------------------------------------------------------------------------------------+")
							print ("     | BestChatBot: Its great to hear that we got your internet back, have a good day!")
							print ("     +-------------------------------------------------------------------------------------------------+")
							break
						elif userInput4 == "No" or userInput4 == "no":
							print ("     +-------------------------------------------------------------------------------------------------+")
							print ("     | BestChatBot: We will need a tech to check the connection, check for available techs, pls wait...|")
							print ("     +-------------------------------------------------------------------------------------------------+")
							time.sleep(3)  # Es posible cambiar el numero
							evento.set()
							print ("     +-------------------------------------------------------------------------------------------------+")
							print ("     | Somebody will be showing today...have a good day.		        		       |")
							print ("     +-------------------------------------------------------------------------------------------------+")
							break
			elif userInput1 == "Yes" or userInput1 == "yes":
				print ("     +-------------------------------------------------------------------------------------------------+")
				print ("     | Please check your internet connection...							       |")
				print ("     +-------------------------------------------------------------------------------------------------+")
				break
		elif userInput == "ASO":
			print ("     +-------------------------------------------------------------------------------------------------+")
			print ("     | BestChatBOT: Do you have a poweroutage?					               	       |")
			print ("     +-------------------------------------------------------------------------------------------------+")
			userInput5 = raw_input("     | Username >>> ")
			if userInput5 == "No" or userInput5 == "no":
				print ("     +-------------------------------------------------------------------------------------------------+")
				print ("     | BestChatBOT:Make sure the ONT its connected to the poweroutlet, do you have services now?       |")
				print ("     +-------------------------------------------------------------------------------------------------+")
				userInput6 = raw_input("     | Username >>> ")
				if userInput6 == "No" or userInput6=="no":
					print ("     +-------------------------------------------------------------------------------------------------+")
					print ("     | BestChatBot: We will need a tech to check the connection, check for available techs, pls wait...|")
					print ("     +-------------------------------------------------------------------------------------------------+")
					time.sleep(3)  # Es posible cambiar el numero
					evento.set()
					print ("     +-------------------------------------------------------------------------------------------------+")
					print ("     | Somebody will be showing today...have a good day.		        		       |")
					print ("     +-------------------------------------------------------------------------------------------------+")
					break
				elif userInput6 == "Yes" or userInput6 == "yes":
					print ("     +-------------------------------------------------------------------------------------------------+")
					print ("     | BestChatBot: Its great to hear that we got your services back, have a good day!")
					print ("     +-------------------------------------------------------------------------------------------------+")
					break
		elif userInput == "ACO":
			print ("     +-------------------------------------------------------------------------------------------------+")
			print ("     | BestChatBot: What do you see on the T.V., nosignal or a blackscreen?")
			print ("     +-------------------------------------------------------------------------------------------------+")
			userInput7 = raw_input("     | Username >>> ")

			if userInput7 == "nosignal":
				print ("     +-------------------------------------------------------------------------------------------------+")
				print ("     | BestChatBOT: Press the input button on the T.V. and change it to the proper one, is it working? |")
				print ("     +-------------------------------------------------------------------------------------------------+")
				userInput8 = raw_input("     | Username >>> ")
				if userInput8 == "Yes" or userInput8 == "yes":
					print ("     +-------------------------------------------------------------------------------------------------+")
					print ("     | BestChatBot: Its great to hear that we got your services back, have a good day!")
					print ("     +-------------------------------------------------------------------------------------------------+")
					break
				elif userInput8 == "No" or userInput8 == "no":
					print ("     +-------------------------------------------------------------------------------------------------+")
					print ("     | BestChatBot: Please call the manufacter of your Television, if it doesnt work call us back.")
					print ("     +-------------------------------------------------------------------------------------------------+")
					break
			elif userInput7 == "blackscreen":
				print ("     +-------------------------------------------------------------------------------------------------+")
				print ("     | BestChatBOT: Please make sure that the Television its connected to the poweroutlet,does it work?|")
				print ("     +-------------------------------------------------------------------------------------------------+")
				userInput9 = raw_input("     | Username >>> ")
				if userInput9 == "Yes" or userInput9=="yes":
					print ("     +-------------------------------------------------------------------------------------------------+")
					print ("     | BestChatBot: Its great to hear that we got your services back, have a good day!")
					print ("     +-------------------------------------------------------------------------------------------------+")
					break
				elif userInput9 == "No" or userInput9=="no":
					print ("     +-------------------------------------------------------------------------------------------------+")
					print ("     | BestChatBot: Please call the manufacter of your Television, if it doesnt work call us back.")
					print ("     +-------------------------------------------------------------------------------------------------+")
					break
		elif userInput == "Billing":
			print ("     +-------------------------------------------------------------------------------------------------+")
			print ("     | BestChatBOT: We will need to transfer you to billing, please call them at 1-800-Billing         |")
			print ("     +-------------------------------------------------------------------------------------------------+")
			print ("     			Loading program, please wait...\n")
			print("")
			for i in range(21):
    						sys.stdout.write('\r')
    						sys.stdout.write("     			[%-20s] %d%%" % ('='*i, 5*i))
    						sys.stdout.flush()
    						sleep(0.25)
			break
		elif userInput == "exit":
			os.system('clear')
			break
        	else:
            		print("     | I did not understand what you said							       |")

else:
	print ("\n     | Usuario incorrecto.\n")
