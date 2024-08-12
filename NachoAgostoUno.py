def registrar_notas():
    notas_materias = []  
    
    while True:
        nota = input("Ingrese la nota de la materia (o 'fin' para terminar): ")
        
        if notas_materias() == 'fin':  
            break
            
        try:
            nota = float(nota)  
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            continue
            
        if 0 <= nota <= 10:  # Verificación del rango de la nota
            notas_materias.append(nota)  # Almacena la nota en la lista
        else:
            print("Nota inválida. La nota debe estar entre 0 y 10.")
    
    if notas_materias:  # Verifica que se hayan ingresado notas
        promedio = sum(notas_materias) / len(notas_materias)  # Calcula el promedio
        print(f"Promedio de notas: {promedio:.2f}")  # Muestra el promedio
        
        if promedio >= 6:  # Verifica si el promedio es suficiente para aprobar
            print("El estudiante ha aprobado.")
        else:
            print("El estudiante no ha aprobado.")
    else:
        print("No se ingresaron notas.")
        
registrar_notas()
