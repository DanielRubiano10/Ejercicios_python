#realiza un programa que revise los numero de una lista y cuente cuantos son positivos y cuantos son negativos 

entradaNum= input("Ingrese los numeros, separados por espacios: ")

numeros= []
for item in entradaNum.split():
    try:
        numeros.append(int(item))
    except ValueError:
        print(f'"{item}"No es un numero entero no sera tomado.')

positivos= 0 
negativos= 0 
listPositivos= []
listNegativos= []
for numero in numeros:
    if numero > 0:
        positivos +=1
        listPositivos.append(numero)
    elif numero < 0:
        negativos +=1
        listNegativos.append(numero)
print(f'los numeros positivos son {positivos}: {listPositivos}')
print(f'los numeros negativos son {negativos}: {listNegativos}')
 
