#realizar un programa que coloque una nota de acuero a una calificacion
#
#pedir calificacion
#
#0-10 rajo
#10-30 raspando
#30-60 masomenos
#60-80 bien
#80-100 excelente

while True:
    try:
        print("*Promedio de calificaciones*")
        cantNotas =(input("numero de calificaciones que desea ingresar"))
        
        
        if not cantNotas.isdigit():# Verificar que la entrada sea numérica
            print("Debe ingresar un número válido para la cantidad de calificaciones.")
            continue
        
        cantNotas = int(cantNotas)  # Convertir a entero después de la verificación
        print("Digite 1 a 1 las notas que va a ingresar usando decimales con (.) y no con (,).")
        print("Las notas deben estar entre un rango de 0 a 100.")
        
        notas = []
                
        for i in range(cantNotas):
            while True:
                try:
                    nota = int(input(f"Ingrese la nota {i+1}: "))
                    if 0 <= nota <= 100:
                        notas.append(nota) #aqui añadimos la nota si esta en el rango
                        break
                    else:
                        print("La nota debe estar entre 0 y 100.")
                except ValueError:
                    print("Por favor, ingrese una nota válida.")
                    
        #codigo a ejecutar
        promedio = sum (notas) / len(notas) # len() permite obtener la cantidad de notas para ser divididas por el promedio obtenido
        print(f"el promedio de las notas es:{promedio}")
        
        if 0 <= promedio <=10:
            print(f"{promedio} ha perdido la materia ")
        elif 10 <= promedio <=30:
            print(f"{promedio} debe presentar examen adicional para poder pasar")
        elif 30 <= promedio < 60:
            print(f"{promedio} debe presentar un trabajo extra")
        elif 60 <= promedio < 80:
            print(f"{promedio} aprobo la materia")
        elif 80 <= promedio <=100:
           print(f"{promedio} calificacion excelente")     
        else:
            print("promedio fuera del rango")
            
        repetir = input("¿Desea realizar otra operacion? \n "
                        "1) Si\n"
                        "2) No\n")
        if repetir == "2":        
            print("menos mal ")
            break          
       
    
    except ValueError:
        print("Por favor, ingrese un número válido.")