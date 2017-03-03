lista1 = [56, "Grupo",[665, 56], "Sistemas", 6, 8,[55656, 588], "programas",456, 566, 565656, "Analistas",[98989,84545,2323], "5", "Hector","otros","ITT","alumnos","Materias", "vacaciones", ["aulas"], "Automatas"]

print(lista1)
lista1[3] = "Carrera"
print (lista1[3])
print(lista1)
lista1[1] = "Cambio"
print(lista1[1])

print(lista1[12][2])
lista1[12][2] = 5656
print(lista1[12][2])

print (lista1[7])
lista1[7] = "Temario"
print (lista1[7])

print (lista1[20])
lista1[20] = "Salones"
print (lista1[20])

lista1.append("Direccion")
print(lista1)

print(lista1[22])
lista1[22]="Departamento"
print(lista1[22])

print (lista1[15])
lista1.insert(15,"HOLIS")
lista1.insert(2,"HOLIS1")
lista1.insert(30,"HOLIS2")
lista1.insert(40,"HOLIS3")
lista1.insert(5,"HOLIS4")
lista1.insert(6,"HOLIS5")
lista1.insert(8,"HOLIS6")

##Buscar elementos en la lista 35, 12, 7, 9, 11, 5, 14

##print(lista1[35]) NO EXISTE ESTA POSICION EN LA LISTA

print(lista1[12])
print(lista1[7])
print(lista1[9])
print(lista1[11])
print(lista1[5])
print(lista1[14])

print(lista1)
print (lista1[29])

lista1.remove("HOLIS3")

print (lista1)

lista2 = [4565,"Es", [665, 56],"Viernes",6, 8,[5, 88,], "Errror", 456, 566 , "565656", "Analistas",[9.9989,84,545,28923],26, 98 ,"Python", "lenguasjes"]

lista2.extend(range(1,21))

print (lista2)

newlist = lista1 + lista2

print ("Nueva Linea")
print (newlist)