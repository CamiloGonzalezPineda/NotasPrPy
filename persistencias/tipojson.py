import json
import os

ARCHIVO_JSON = "productos.json"

def guardar_productos_json(productos):
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as f:
        json.dump(productos, f, indent=4, ensure_ascii=False)
    print(f'INVENTARIO GUARDADO EN LA RUTA: {ARCHIVO_JSON}')

def cargar_productos_json():
    if not os.path.exists(ARCHIVO_JSON):
        print('no existe')
        return []
    with open(ARCHIVO_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)
