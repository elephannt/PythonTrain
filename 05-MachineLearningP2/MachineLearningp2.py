from sklearn import tree

##En este caso, el primer valor, es la altura en cms, si es mayor a 150 muy problablemente sea adulto.
##si la altura es menor, muy probablemente sea un infante
## 1 = adulto, y 0 = es para infante.
## la variable carac se podria ver como [altura,peso].

caracteristicas = [[180,80],[170,70],[140,30],[130,20]]
etiquetas = [1,1,0,0]

##estamos creando un arbol para el algoritmo de desicion.

clasif = tree.DecisionTreeClassifier()

##.fit es para encontrar patrones en datos

clasif = clasif.fit(caracteristicas,etiquetas)
print ("Si es 1 = Adulto, si es 0 = Infante: ")
print (clasif.predict([[180,60]]))


