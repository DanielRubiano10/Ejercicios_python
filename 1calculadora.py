while True:
    try:
        print("CALCULADORA")
        operacion = input("¿Qué operación desea realizar?\n"
                          "1) suma\n"
                          "2) resta\n"
                          "3) multiplicación\n"
                          "4) división\n"
                          "5) Salir\n")
        
        if operacion.lower() == "salir" or operacion == "5":
            print("Adiós")
            break

        num1 = int(input("Ingrese un número: "))
        num2 = int(input("Ingrese otro número: "))
        
        if operacion == "suma" or operacion == "1":
            resultado = num1 + num2
            print(f" el resultado de {num1} + {num2} = {resultado}")

        elif operacion == "resta" or operacion == "2":
            resultado = num1 - num2
            print(f"El resultado de {num1} - {num2} = {resultado}")

        elif operacion == "multiplicación" or operacion == "3":
            resultado = num1 * num2
            print(f"El resultado de {num1} * {num2} = {resultado}")

        elif operacion == "división" or operacion == "4":
            if num2 == 0:
                print("no es posible dividir por (0)")
            else:
                resultado = num1 / num2
                print(f"El resultado de {num1} / {num2} = {resultado}")
        else:
            print("Operación no válida")
            continue

        repetir = input("¿Desea realizar otra operación? (1-para SI, 2-para NO): ")
        if repetir == "2":
            print("Hasta pronto")
            break

    except ValueError:
        print("Error: Debe ingresar un número válido.")
        continue