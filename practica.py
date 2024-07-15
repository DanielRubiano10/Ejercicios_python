#listas por comprension: es hacer una lista que internamente se opere para dar un resultado a la lista
"""numeros = [x * 2 for x in range(1, 6)]
print(numeros)

#lista por extension
numeros= []
for x in range (1,6):
    numeros.append(x*2)
print(numeros)

#OPERADOR TERNARIO:
#lloviendo= False
#acessorio= "paraguas" if lloviendo else "gafas de sol "
#print(acessorio)

import pandas as pd
def sumarDos(x):
 return x+2

datos=pd.DataFrame({"numeros":[1,2,3,4,5,6,7,8,9,5,2,1,21,55,12,]})
datos ["numeros_mas_dos"] = datos["numeros"].apply(sumarDos)
print(datos)"""""

import math
print(math.sqrt(16))





