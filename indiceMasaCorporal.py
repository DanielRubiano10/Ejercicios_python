#programa que imprime los numeros del 1 al 10 bucle for 

#for x in range(1, 10):
#print(x)
 
#programa que mide si debe aumentar su cantidad de ejercicio diario. 
def indiceMasaCorporal(peso, altura):
    imc = peso / (altura **2)
    return imc

numUsuarios=int (input("Ingrese el numero de usuarios: "))
for _ in range(numUsuarios):
    nombre= (input("ingrese su nombre!: "))
    edad= int(input("ingrese su edad!: "))
    peso= float(input("ingrese su peso en kg: "))
    altura= float(input("ingrese su altura en cm: ")) / 100 #convierte altura de cm a m    '

    imc= indiceMasaCorporal(peso, altura) 
    print(f"{nombre}, su indice de masa corporal es: {imc:.1f}")

    if 0 <= imc <= 18.5:
        print('esta muy delgado debe mejorar su alimentacion pronto y entrenar 2 veces por semana.! ') 
    elif 18.5 <= imc <= 24.9:
        print('tiene un peso promedio si lo quisiera podria aumentar alguna practica deportiva de su gusto y mejoraria un poco mas. ')
    elif 25.9 <= imc <= 29.9:
        print('tiene buena masa corporal no olvidar la resistencia cardiovascular para cuidar el corazon. ')
    elif imc > 29.9:
        print ('pronto debes empezar a realizar ejercicio si quiere cuidar su vida y su salud para el futuro. ')       
    else:
        print('El IMC calculado esta fuera del rango, porfavor revise los datos ingresados')
    
    
    
