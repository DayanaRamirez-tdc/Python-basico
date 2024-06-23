#Intercambiar los valores de dos variables con asignacion multiple

a = int(input("Escoge un valor: "))
b = int(input("Escoge un segundo valor: "))

a, b = b, a

print(a, b)