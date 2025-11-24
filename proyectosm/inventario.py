
from datos import inventario

def mostrar_inventario():
    if not inventario:
        print("No hay productos en inventario.")
        return
    print(f'{"NOMBRE":<25}{"MARCA":<20}{"CATEGORIA":<20}{"PRECIO":<15}{"STOK":<10}{"GARANTIA":<10}')
    print("-"*100)
    for p in inventario:
        print(f'{p["nombre"]:<25}{p["marca"]:<20}{p["categoria"]:<20}{p["precio"]:<15}{p["stok"]:<10}{p["garantia"]:<10}')

def agregar_producto():
    nombre = input("Nombre: ")
    marca = input("Marca: ")
    categoria = input("Categoría: ")
    precio = float(input("Precio: "))
    stok = int(input("Stock: "))
    garantia = int(input("Garantía meses: "))
    inventario.append({
        "nombre": nombre,
        "marca": marca,
        "categoria": categoria,
        "precio": precio,
        "stok": stok,
        "garantia": garantia
    })
    print("Producto agregado correctamente.")

def buscar_producto(nombre):
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None

def actualizar_producto():
    nombre = input("Nombre del producto a actualizar: ")
    prod = buscar_producto(nombre)
    if not prod:
        print("Producto no encontrado.")
        return
    nuevo_nombre = input(f"Nuevo nombre [{prod['nombre']}]: ") or prod['nombre']
    nueva_marca = input(f"Nueva marca [{prod['marca']}]: ") or prod['marca']
    nueva_categoria = input(f"Nueva categoría [{prod['categoria']}]: ") or prod['categoria']
    nuevo_precio = input(f"Nuevo precio [{prod['precio']}]: ") or prod['precio']
    nuevo_stok = input(f"Nuevo stock [{prod['stok']}]: ") or prod['stok']
    nueva_garantia = input(f"Nueva garantía [{prod['garantia']}]: ") or prod['garantia']

    prod.update({
        "nombre": nuevo_nombre,
        "marca": nueva_marca,
        "categoria": nueva_categoria,
        "precio": float(nuevo_precio),
        "stok": int(nuevo_stok),
        "garantia": int(nueva_garantia)
    })
    print("Producto actualizado correctamente.")

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    prod = buscar_producto(nombre)
    if not prod:
        print("Producto no encontrado.")
        return
    confirm = input("¿Desea eliminar el producto? (si/no): ").lower()
    if confirm == "si":
        inventario.remove(prod)
        print("Producto eliminado.")
    else:
        print("Acción cancelada.")
