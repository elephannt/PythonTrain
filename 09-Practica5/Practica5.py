#!/usr/local/bin/python
# -*- coding: utf-8 -*-
class coche:

    def __init__ (self,carrera):
        self.carrera = carrera

    def manejar (selfs):
        print ("Estoy feliz manejando")

    def correr (self):
        print("Asi corres tu")
        print ("Son",self.carrera," Km")

##para que imprima
carro1 = coche ("a")
carro2 = coche(30)
carro1.manejar()
carro2.correr()

class Porch(coche):
    pass

class Camarro(coche):
    pass

##haces algo con el camaro
Camarro = Camarro(30)
Camarro.correr()
##haces algo con el porsh
Porch = Porch("Feliz")
Porch.manejar()


##Inicia programa
##Crear un objeto instrumento con los atributos y métodos comunes e indicar al programa
##que flauta, batería, guitarra y saxofón son tipos de instrumentos, haciendo que hereden de instrumento

class instrumento:
    def __init__ (self,instrumento):
        self.instrumento = instrumento

    def tocar (selfs):
        print ("Estoy feliz tocando un instrumento")

    def envivo (self):
        print("Te la rifas tocando...")
        print ("Estas tocando...",self.instrumento)


class flauta(instrumento):
    pass

class baeria(instrumento):
    pass
class guitarra(instrumento):
    pass

class saxofon(instrumento):
    pass
##Creamos las clases, pero es importante instanciarlas ya que si no, no hace nada el programa.

ins1 = instrumento ("flauta")
ins1.envivo()

flauta = flauta("flauta")
flauta.envivo()
baeria=baeria("bateria")
baeria.envivo()
guitarra =guitarra("guitarra")
flauta.envivo()
saxofon = saxofon("saxofon")
saxofon.envivo()