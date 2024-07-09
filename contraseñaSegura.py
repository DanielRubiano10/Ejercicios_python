'''prograna que valide si una contraseña es segura.
-> tiene mas de 8 caracteres?
-> tiene  al menos una letra mayuscula?
-> tiene al menos un numero?'''


def comprobarContraseña(password):
    largo= False
    mayuscula= False
    numeros= False
    
    if len(password) >8:#funcion contar longitud de un string
        largo= True 
    for i in range(len(password)):
        if password [i].isupper():#funcion validar si hay mayusculas
            mayuscula = True
        if password [i].isnumeric():#funcion para saber si hay numeros
             numeros = True   
        
    if largo and mayuscula and numeros:
        return True
    else:
        return False

password = input("ingrese una contraseña: ")
verificacion = comprobarContraseña(password)

if verificacion:
    print("La contraseña es segura")
else:
    print("La contraseña no es segura")