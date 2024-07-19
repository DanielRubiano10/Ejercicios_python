import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
rutaArchivo = 'data/Mrbeast_stats.csv'
datos = pd.read_csv(rutaArchivo)

# Mostrar las columnas del DataFrame para verificar los nombres
print(datos.columns)

# Ordenar los datos por la cantidad de vistas en orden descendente
datosOrdenados = datos.sort_values(by='Views', ascending=False)

# Seleccionar las primeras 10 filas para una mejor visualización
topVideos = datosOrdenados.head(10)

# Crear el gráfico de barras
plt.figure(figsize=(12, 6))
plt.barh(topVideos['Title'], topVideos['Views'], color='skyblue')
plt.gca().invert_yaxis()  # Invertir el eje y para mostrar el video con más vistas arriba

# Añadir títulos y etiquetas
plt.title('Top 10 Videos de MrBeast por Reproducciones')
plt.xlabel('Reproducciones')
plt.ylabel('Título del Video')

# Añadir etiquetas con la fecha y el enlace del video
for index, row in topVideos.iterrows():
    plt.text(row['Views'], index, f"{row['Date']} - {row['Link']}", ha='right', va='center', fontsize=8)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
