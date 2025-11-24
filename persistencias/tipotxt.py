import os

ARCHIVO_TXT = "productos.txt"

def guardar_productos_txt(productos):
    if not productos:
        with open(ARCHIVO_TXT, 'w', encoding='utf-8') as f:
            f.write('Nombre,Precio,Cantidad\n')
        print(f'INVENTARIO GUARDADO EN LA RUTA: {ARCHIVO_TXT}')
        return

    with open(ARCHIVO_TXT, 'w', encoding='utf-8') as f:
        f.write(','.join(productos[0].keys()) + '\n')
        for producto in productos:
            f.write(','.join(str(value) for value in producto.values()) + '\n')
    print(f'INVENTARIO GUARDADO EN LA RUTA: {ARCHIVO_TXT}')

def cargar_productos_txt():
    if not os.path.exists(ARCHIVO_TXT):
        print('no existe')
        return []

    productos = []
    with open(ARCHIVO_TXT, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        if not lineas:
            return []
        encabezados = lineas[0].strip().split(',')
        for linea in lineas[1:]:
            valores = linea.strip().split(',')
            productos.append(dict(zip(encabezados, valores)))
    return productos
