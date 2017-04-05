import threading, time

#Ejemplo uno

# class MiThread(threading.Thread):
# 	def __init__(self, num):
# 		threading.Thread.__init__(self)
# 		self.num = num
#
# 	def run(self):
# 		print "Ejecucion de hilo", self.num
#
# print "El hilo principal"
#
# for i in range(0, 80):
# 	t = MiThread(i)
# 	t.start()
# 	t.join()

#Ejemplo 2

# def imprime(num):
#     print("El hilo",num)
# print("El hilo principal")
#
# for i in range(0,10):
#     t = threading.Thread(target=imprime,args=(i,))
#     t.start()

#Ejemplo 3

# lista = []
# lock = threading.Lock()
# def anyadir(obj):
#     lock.acquire()
#     lista.append()
#     lock.release()
# def obtener():
#     lock.acquire()
#     obj=lista.pop()
#     lock.release()

#Ejemplo 4

class MiThread(threading.Thread):
    def __init__(self,evento):
        threading.Thread.__init__(self)
        self.evento=evento
    def run(self):
        print (self.getName(),"En espera del evento")
        self.evento.wait()
        print (self.getName(),"Fin del evento")

evento = threading.Event()

#
# #Espera del evento
#
# time.sleep(3) #Es posible cambiar el numero
# evento.set()

A = 270
B = 340
C = 390
total = 0
menu = '1'
print ("\n")
print ("     +--------------------------+")
print("     |    Inicio del programa   |")
print ("     +--------------------------+")

print ("     +----------------------------------------------------+")
print ("     |  Que comida desea el dia de hoy?                   |")
print ("     |  Comida 1 = 270 , Comida 2 = 340 , Comida 3 = 390  |")
print ("     +----------------------------------------------------+")


comida = raw_input("     | Eliga la comida por favor >> ")

if comida == '1':

    cantidad = int(raw_input("     | Solo aceptamos monedas de 10$ , 50$ y 100$, por favor ingrese la cantidad de: 270 >>"))
    if cantidad == 10 or cantidad == 50 or cantidad == 100:
        while cantidad <= A:
               # print "     | Ingrese dinero, por favor, lleva la cantidad de: %s" %cantidad
                dinero = int(raw_input("     | Ingrese dinero, por favor, lleva la cantidad de >>"))
                print "     | La cantidad va en: ", cantidad
                if dinero == 10 or dinero == 50 or dinero == 100:
                    cantidad = cantidad + int(dinero)
                else:
                    print "     | Cantidad incorrecta: ",dinero
                    break

        if cantidad > A:
                print "     | Por favor espere, calculando..."
                time.sleep(3) #Es posible cambiar el numero
                evento.set()
                print "     | Intente de nuevo, se le regresa: ", cantidad


    else:
        print "Cantidad incorrecta: ", cantidad

elif comida == '2':

    cantidad = int(raw_input("     | Solo aceptamos monedas de 10$ , 50$ y 100$, por favor ingrese la cantidad de: 340 >>"))
    if cantidad == 10 or cantidad == 50 or cantidad == 100:
        while cantidad <= B:
            dinero = int(raw_input("     | Ingrese dinero, por favor, lleva la cantidad de >>"))
            print "     | La cantidad va en: ", cantidad
            if dinero == 10 or dinero == 50 or dinero == 100:
                cantidad = cantidad + int(dinero)
            else:
                print"     | Cantidad incorrecta: ", dinero
                break
        if cantidad > B:
            print "     | Por favor espere, calculando..."
            time.sleep(3)  # Es posible cambiar el numero
            evento.set()
            print "     | Intente de nuevo, se le regresa: ", cantidad

    else:
        print "     | Cantidad incorrecta: ", cantidad

elif comida == '3':

    cantidad = int(raw_input("      | Solo aceptamos monedas de 10$ , 50$ y 100$, por favor ingrese la cantidad de: 390 >>"))
    if cantidad == 10 or cantidad == 50 or cantidad == 100:
        while cantidad <= C:
            dinero = int(raw_input("     | Ingrese dinero, por favor, lleva la cantidad de >>"))
            print "     | La cantidad va en: ", cantidad
            if dinero == 10 or dinero == 50 or dinero == 100:
                cantidad = cantidad + int(dinero)
            else:
                print "     | Cantidad incorrecta: ", dinero
                break
        if cantidad > C:
            print "     | Por favor espere, calculando..."
            time.sleep(3)  # Es posible cambiar el numero
            evento.set()
            print "     | Intente de nuevo, se le regresa: ", cantidad

    else:
        print ("     | Cantidad incorrecta: ", cantidad)

else:

    print "     | Esa comida no existe: ", comida
    print ("     +--------------------------+")




















