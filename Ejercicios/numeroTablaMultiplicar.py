#programa que calcula la tabla de multiplicar del numero entero ingresado por el usuario del 0 al 12 

def tablaDeMultiplicar(n1, n2):
    return str(n1) + "*" + str(n2) + "=" + str(n1*n2)


n= int(input("Ingrese un numero entero: "))
for i in range(0, 11):
 print(tablaDeMultiplicar(n,i))
