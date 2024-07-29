# Solicita al usuario que ingrese 10 números
numeros = []
for i in range(10):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

# Filtra los números pares
numeros_pares = [numero for numero in numeros if numero % 2 == 0]

# Imprime la lista de números pares
print("Números pares ingresados:", numeros_pares)
