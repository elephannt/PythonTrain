##CREATED BY MARCO.

t = ("a","b","python","z","Ejemplo1")

print(t)
print (t[-1])
print (t[-1])
print (t[-5])
print (t[0])
print (t[1:3])

li = ["a","b","python","z","Ejemplo3"]

print(li)
print(li[0])
print(li[0])
print(li[4])

print(li)
print(li[-0])
print(li[-4])

print(li[1:3])
print(li[1:-1])
print(li[0:3])

print(li[:3])
print(li[3:])
print(li[:])

li.append("new")
li.insert(2,"new")
li.insert(2,"z")
li.insert(2,"example")
li.insert(2,"e")
li.extend(["two","elements"])

li.index("example")
li.index("new")
li.index("z")
li.index("e")

li.remove("z")
li.remove("new")
li.remove("a")
li.pop()


li = ['a','b','ejemplo3']
li = li + ['ejemplo2','new']
li += ['two']
li = [1,2] * 3

print (li)