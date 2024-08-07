print("Este programa cuenta la cantidad de vocales")
frase = input("Ingrese la frase o palabra: ")

contador_vocales = 0

for i in frase:  
    if i in "aeiouAEIOU":
        print(i, end=" ")
        contador_vocales += 1
    else:
        print(i, end="")

print(f"\nLa cantidad total de vocales en la frase es de: {contador_vocales}")
