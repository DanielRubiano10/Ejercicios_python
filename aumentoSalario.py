#calcule el nuevo salario de un trabajados si tuvo un aumento del x%
 
def calcularAumento(salario, x):
    nuevoSalario= salario + (salario * (x/100))
    return nuevoSalario 
try: 
    salarioActual= float(input("Ingrese su salario actual: ").replace(',','.'))
    aumento= float(input("ingrese el porcentaje de incremento que tendra el salario: ").replace(',','.')) 
    nuevoSalario= calcularAumento(salarioActual,aumento)

    print("El nuevo salario del trabajador es de: ", nuevoSalario)
except ValueError:
    print("porfavor ingrese un numero valido")                    