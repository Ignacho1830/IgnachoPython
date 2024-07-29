print("Este programa cuenta la cantidad de letras")
palabra = input("Ingrese la frase o palabra: ")

contador_vocales = 0

for i in palabra:  
    if i == "a":
        print (i, end="")
    elif i == "e":
        print (i, end="")
        i == "i"
        print (i, end="")
        i == "o"
        print (i, end="")
        i == "u"
        print(i, end="")
    else:
        print (i, end="")
        contador_vocales += 1

print(f"\nLa cantidad total de letras en la frase es: {contador_vocales}")
