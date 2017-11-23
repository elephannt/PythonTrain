from sklearn import tree

## In this case, the first value, is the height in cms, if it is greater than 150, it is probably adult.
## If the height is lower, it is very likely that it is an infant
## 1 = adult, and 0 = is for an infant.
## the variable carac could be seen as [height, weight].

caracteristicas = [[180,80],[170,70],[140,30],[130,20]]
etiquetas = [1,1,0,0]

## we are creating a tree for the desicion algorithm.
clasif = tree.DecisionTreeClassifier()

##. fit is to find patterns in data

clasif = clasif.fit(caracteristicas,etiquetas)
print ("If its 1 = Adult, if 0 = child: ")
print (clasif.predict([[180,60]]))


