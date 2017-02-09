## primera forma
class ArbolBinario:
    def __init__(self, elemento, esMenorFunction=lambda x, y: x < y):
        self.derecha = None
        self.isquierda = None
        self.elemento = elemento
        self.esMenor = esMenorFunction


## Segunda forma
class Arbol:
    def __init__(self, carga=None, isq=None, der=None):
        self.carga = carga
        self.isquierda = isq
        self.derecha = der

    def __str__(self):
        return str(self.carga)


def suma(arbol):
    if arbol == None: return 0
    return suma(arbol.isquierda) + suma(arbol.derecha) + arbol.carga


arbol = Arbol(2, Arbol(7,Arbol(2),Arbol(6,Arbol(5),Arbol(11,Arbol(5),Arbol(9,Arbol(4))))))
arbol1 = Arbol(5, Arbol(24,Arbol(5),Arbol(7,Arbol(8),Arbol(11))))
arbol2 = Arbol(2, Arbol(7,Arbol(2),Arbol(6,Arbol(5),Arbol(11,Arbol(5),Arbol(9)))))
arbol3 = Arbol(2, Arbol(7,Arbol(2),Arbol(6,Arbol(5),Arbol(11,Arbol(5),Arbol(9,Arbol(4,Arbol(5)))))))
arbol4 = Arbol(2, Arbol(7,Arbol(2),Arbol(6,Arbol(5),Arbol(11,Arbol(5),Arbol(9,Arbol(4,Arbol(5,Arbol(4,Arbol(5,Arbol(4,Arbol(5)))))))))))
print suma(arbol)
print suma(arbol1)
print suma(arbol2)
print suma(arbol3)
print suma(arbol4)