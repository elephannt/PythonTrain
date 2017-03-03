


##Ejecute uno por uno el sig codigo de conjuntos
T = ['Practica','Practica','Tareas','Tareas','Grupo','Grupo','Grupo']
conjuntoT=set(T)
print(conjuntoT)
##Uso del set par union
A=set([1,2,3,4,5,20,34,25])
B=set([3,4,5,6,7,20,40,60])

print(A|B)
##Uso del set para interseccion
A=set([1,2,3,4,5,20,34,25,89,100])
B=set([3,4,5,6,7,20,40,70,7,60])
print (A&B)
##Uso de la diferencia
A=set([1,7,3,4,5,20,34,25])
B=set([3,4,5,6,7,20,40,7,60])
print (A-B)
##uso de set pertenencia
A=set([1,2,3,4,5,8,35,23,90])
print(6 in A)
print(1 not in A)
print(56 in A)
print(68 not in A)
print(1 not in B)

##Inicia program
print("\nQue tamano gusta?\n1=chico 10$\n2=mediano 20$\n3=grande 30$\n")
tamano = raw_input()
F = set([tamano])
print (F)
print("Frutas: 1=Manzana,2=Pera,3=Aguacate,4=Sandia,5=Durazno")
frutas = raw_input()
J = set([frutas])
print (J)
##print ("Quieres ingredientes extra? si=1,no=0")
##menu = raw_input()
menu = '1'
precio = 0

while menu == '1':

    print ("Quieres ingredientes extra?\nsi=1 + 10$ precio solo una ves.\nno=0 + 0$")
    menu = raw_input()

    if menu == '0':

        if tamano == '1':
            precio = 10
        elif tamano == '2':
            precio = 20
        elif tamano == '3':
            precio = 30
        break

    print("Frutas: 1=Manzana,2=Pera,3=Aguacate,4=Sandia,5=Durazno\n")
    frutas = raw_input()
    J.add(frutas)

if len(J) > 1:
    precio = precio + 10

print(J | F)
print (precio)





