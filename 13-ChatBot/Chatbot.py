import random, threading, time

#Patron singleton

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
random_greeting = random.choice(greetings)

question = ['How are you?','How are you doing?']
responses = ['Okay',"I'm fine"]
random_response = random.choice(responses)

print ("\n     +-------------------------------------------------------------------------------------------------+")
user = raw_input("	 | Please enter your username: ")
password = raw_input("	 | Please enter your password: ")
print ("	 | Going to verify information, please wait...")
time.sleep(3)  # Es posible cambiar el numero
evento.set()

while True:
	print ("     +-------------------------------------------------------------------------------------------------+")
	print ("     |									    WELCOME BACK									  		   |")
	print ("     +-------------------------------------------------------------------------------------------------+")
	print ("     | CCON: Cannot connect on network						  								  		   |")
	print ("     | ASO: All services out								  								  		   |")
	print ("     | ACO: All channels out								  								  		   |")
	print ("     | PHYS: Physical condition								  								  		   |")
	print ("     +-------------------------------------------------------------------------------------------------+")

	userInput = raw_input("     | Username >>> ")
	if userInput in greetings:
		print(random_greeting)
	elif userInput in question:
		print(random_response)

	elif userInput == "CCON":
		print ("     +-------------------------------------------------------------------------------------------------+")
		print ("     | BestChatBOT: Do you have any lights on the BHR?									               |")
		print ("     +-------------------------------------------------------------------------------------------------+")
		userInput1 = raw_input("     | Username >>> ")
		if userInput1 == "No" or userInput1 == "no":
			print ("     +-------------------------------------------------------------------------------------------------+")
			print ("     | BestChatBOT: Make sure that the BHR its connected to the poweroutlet. Do you have lights?	   |")
			print ("     +-------------------------------------------------------------------------------------------------+")
			userInput2 = raw_input("     | Username >>> ")
			if userInput2 == "Yes" or userInput2 == "yes":
				print ("     +-------------------------------------------------------------------------------------------------+")
				print ("     | BestChatBot: Do you have internet connection										  		       |")
				print ("     +-------------------------------------------------------------------------------------------------+")
				userInput3 = raw_input("     | Username >>> ")
				if userInput3 == "Yes" or userInput3 == "yes":
					print ("     +-------------------------------------------------------------------------------------------------+")
					print ("     | BestChatBot: Its great to hear that we got your internet back, have a good day!			  	   |")
					print ("     +-------------------------------------------------------------------------------------------------+")
					break
				elif userInput3 == "No" or userInput3 == "no":
					print ("     +-------------------------------------------------------------------------------------------------+")
					print ("     | BestChatBot: We are going to Break the DHCP lease, please wait..								   |")
					print ("     +-------------------------------------------------------------------------------------------------+")
					time.sleep(3)  # Es posible cambiar el numero
					evento.set()
					print ("     +-------------------------------------------------------------------------------------------------+")
					print ("     | BestChatBot: Do you have internet connection now?		 			                           |")
					print ("     +-------------------------------------------------------------------------------------------------+")
					userInput4 = raw_input("     | Username >>> ")
					if userInput4 == "Yes" or userInput4 == "yes":
						print ("     +-------------------------------------------------------------------------------------------------+")
						print ("     | BestChatBot: Its great to hear that we got your internet back , have a good day!			       |")
						print ("     +-------------------------------------------------------------------------------------------------+")
						break
					elif userInput4 == "No" or userInput4 == "no":
						print ("     +-------------------------------------------------------------------------------------------------+")
						print ("     | BestChatBot: We will need a tech to check the connection, check for available techs, pls wait...|")
						print ("     +-------------------------------------------------------------------------------------------------+")
						time.sleep(3)  # Es posible cambiar el numero
						evento.set()
						print ("     +-------------------------------------------------------------------------------------------------+")
						print ("     | Somebody will be showing today...have a good day.									           |")
						print ("     +-------------------------------------------------------------------------------------------------+")
						break
		elif userInput1 == "Yes" or userInput1 == "yes":
			print ("     +-------------------------------------------------------------------------------------------------+")
			print ("     | Please check your internet connection...													       |")
			print ("     +-------------------------------------------------------------------------------------------------+")

			break
	elif userInput == "exit":
		break
        else:
            print("     | I did not understand what you said									|")

