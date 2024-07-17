#programa para controlar el inventario de una empresa(diccionario[])
inventario={}

inventario["best protein"] = {"cantidad": 10, "precio":150.000}
inventario["megaplex"] = {"cantidad":2, "precio":110.000}
inventario["intenze"] = {"cantidad":1, "precio": 100.000}

print("inventario inicial:")
print(inventario)

cantidad_Intenze= inventario["intenze"]["cantidad"]
print(f"cantidad de intenze {cantidad_Intenze}")

inventario ["intenze"]["cantidad"]= 10
print('cantidad de intenze "actualizada: "')
print(inventario["intenze"]["cantidad"])


# Iterar a través de los productos en el inventario
print("\nInventario completo:")
for producto, detalles in inventario.items():
    print(f"Producto: {producto}, Cantidad: {detalles['cantidad']}, Precio: ${detalles['precio']}")