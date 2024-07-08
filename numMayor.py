#ingrese 3 datos numericos diferentes  y reconozca cual de los tres mayor

print('Ingresa 3 numeros diferentes?')
num1=(int(input("ingrese el primer numero")))
num2=(int(input("ingrese el segundo numero")))
num3=(int(input("ingrese el tercer numero numero")))

#numero mayor
if num1 > num2 and num1 > num3:
    mayor = num1
elif num2 > num1 and num2 > num3:
    mayor = num2
elif num3 > num1 and num3 > num2:
    mayor = num3
else:
    mayor = None
 
#numero menor
if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
elif num3 < num1 and num3 < num2:
    menor = num3
else:
    menor = None
#mostrar resultados
if mayor is not None:
    print(f"el numero mayor es: {mayor}")
else:
    print("hay un empate entre los numeros mayores.")
    
if menor is not None:
  print(f"el numero menor es: {menor}")
else:
    print("hay un empate entre los numeros menores.")    



