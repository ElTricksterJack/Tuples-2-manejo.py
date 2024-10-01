from os import system
print(" ")
print("Ruvalcaba Valverde Miguel Angel")
print("--------------------------------------")
print("--Acceso a Tuples de Python--")
union = ("undead","unluck","unfeel","unmove","unfair","untouchable","unstoppable","untruth","unavoidable","unchange","unjustice","unbreakable","unforgettable")
under = ("unseen","unfede","untell","unrepair","undecrease","untrust","unback","undraw","unburn","unchaste")
n = (0,1,2,3,4,5,6,7,8,10)
unor = ("unconsistent","uncompressible","uncompress","uncorporate","unexplorable")
print(union[0])
print(union[1])
print(under[8])
print("----")
print(n[-1])
print(n[-10])#Empiesas a alrebes embes de 0,1,2,3,4,5 con los negativos es 5,4,3,2,1,0 etc
print(under[-7])
print("----")#Esto es para cortar siertas o mostrar los elemetos de una lista en hasta cierto punto
print(n[2:])#Desde :
print(n[:4])#: Hasta
print(n[3:7])# Desde : Hasta
print(n[:-5])
print(n[-2:-5])
print(n[1:-5])# 0 no vale
print("----")
print(union[2:6])
print(union[8:])
print(under[:-3])
print(under[-9:])
KOK = int(input('cualquier dijito NUMERICO pasar de pagina: '))
system("cls")
print("-------Espesificar elementos-------")
if "apple" in union:
  print("si existe un negador inmanzana")
if "unluck" in union:
  print("si existe un negador infortunio, esa chica es un ejemplo a segir")
if "unforgettable" in union:
  print("si existe un negador inolvidable, este es todo un guerrero y mesere ser feliz... hay nico porque")
if "unadaptable" in under:
  print("si existe un negador inadaptable, si llega a existir seria igual que unsleep o unhealthy")
if "unseen" in under:
  print("si existe un negador invisible, ipocrita que pasado trajico es ese Sean")
KOK = int(input('cualquier dijito NUMERICO pasar de pagina: '))
system("cls")
print("-------Contar elementos-------")
print(len(union))
print(len(under))
KOK = int(input('cualquier dijito NUMERICO pasar de pagina: '))
system("cls")
print("-------Actualizar Tuples-------")
#Observe bien los cambios en la lista
print(unor)

#Con esto replasas items de una lista
y = list(unor)
y[1] = "Unlockable"
unor = tuple(y)
print(unor)

#Este es una forma de alladir items a la lista
y = list(unor)
y.append("Unbeatable")
unor = tuple(y)
print(unor)
#Con este tambien allades items a la lista
y = ("Unsurmountable",)
unor += y
print(unor)

#Con esto remueves elementos de una lista
y = list(unor)
y.remove("uncorporate")
unor = tuple(y)
print(unor)
#Con esto puedes borrar listas
del unor
KOK = int(input('cualquier dijito NUMERICO pasar de pagina: '))
system("cls")

print("-------Descomprimir  Tuples-------")
unor1 = ("unconsistent","uncompressible","uncompress","uncorporate","unexplorable")
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
KOK = int(input('cualquier dijito NUMERICO pasar de pagina: '))
system("cls")
print("-----Unir Tuples------")
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
KOK = int(input('cualquier dijito NUMERICO pasar de pagina: '))
system("cls")
"""
print("------Extras-----")
x = n.count(4)
print(x)
x = n.index(7)
print(x)
#Borrar primer item
unor1.pop()
print(unor1)
#tambien puedes borrar items espesificos
unor1.pop(3)
print(unor1)
#alladir items
unor1.insert(1, "uncompetent")
print(unor1)

#puedes fisionar listas con tuples
unfan = ("unlettered","unquantifiable","uncountable","unfathomable")
unor1.extend(unfan)
print(unor1)
unfan2 = ["unequivocal","unspeakable","inexplicable","unmistakable"]
unor1.extend(unfan2)
KOK = int(input('cualquier dijito NUMERICO pasar de pagina: '))
system("cls")
"""
print("-----------")
print("Rresultado: se aprendio de los tuples y sus accesos")
print(" ")
