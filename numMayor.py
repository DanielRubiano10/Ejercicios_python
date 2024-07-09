print('*NUMERO MAYOR NUMERO MENOR*')
print('Ingresa 3 numeros diferentes?')
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)
 
# Mostrar resultados
if mayor is not None:
    print(f"El numero mayor es: {mayor}")
else:
    print("Hay un empate entre los numeros mayores.")
    
if menor is not None:
    print(f"El numero menor es: {menor}")
else:
    print("Hay un empate entre los numeros menores.")   
    
while True:
    repetir = input("¿Desea realizar otra operación? (1-para SI, 2-para NO): ")
    if repetir == "2":
        print("Hasta pronto")
        break
