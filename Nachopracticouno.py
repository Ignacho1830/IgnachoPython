def pares():
 numeros_pares = []
 for i in range(10):
    numero = int(input(f"Ingrese el numero : "))
    if numero % 2 == 0:
        numeros_pares.append(numero)
        print("Numeros pares ingresados son :", numeros_pares)

pares()
