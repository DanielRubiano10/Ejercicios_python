# como trabajar con archivos CSV en python 

import pandas as pd
import os
rutaArchivo='data/Football_teams_price_data.csv'

if not os.path.isfile(rutaArchivo):
    print(f"el archivo {rutaArchivo} no existe.")
else:
    datos= pd.read_csv(rutaArchivo)
    
    print(datos.head())


