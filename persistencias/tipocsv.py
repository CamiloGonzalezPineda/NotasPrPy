import csv
import os

ARCHIVO_CSV = "productos.csv"

def guardar_productos_csv(productos):
    if not productos:
        with open(ARCHIVO_CSV, 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            escritor.writerow(['Nombre', 'Precio', 'Cantidad'])
        print(f'INVENTARIO GUARDADO EN LA RUTA: {ARCHIVO_CSV}')
        return

    with open(ARCHIVO_CSV, 'w', newline='', encoding='utf-8') as f:
        escritor = csv.DictWriter(f, fieldnames=productos[0].keys())
        escritor.writeheader()
        escritor.writerows(productos)
    print(f'INVENTARIO GUARDADO EN LA RUTA: {ARCHIVO_CSV}')

def cargar_productos_csv():
    if not os.path.exists(ARCHIVO_CSV):
        print('no existe')
        return []

    with open(ARCHIVO_CSV, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)
