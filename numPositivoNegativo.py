# Ingresar un numero y devolver si dicho numero es positivo, negativo o es 0

while True:
    try:
        numero = float(input("Ingrese un numero: "))

        if numero > 0:
            print("El numero es positivo")
        elif numero < 0:
            print("El numero es negativo")
        else:
            print("El numero es cero")
        break
    except ValueError:
        print("Error: debe ingresar un numero valido")


