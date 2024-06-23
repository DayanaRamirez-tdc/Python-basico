#Definir si una palabra es palíndromo

palabra = input("Elige una palabra: ")
es_pa = palabra == palabra[::-1]

print("La palabra es un palindromo", es_pa )