
from datos import inventario, ventas

def registrar_venta():
    cliente = input("Nombre del cliente: ")
    tipo_cliente = input("Tipo de cliente: ")
    producto = input("Producto vendido: ")
    cantidad = int(input("Cantidad: "))
    descuento = float(input("Descuento (%): "))

    prod = next((p for p in inventario if p["nombre"].lower() == producto.lower()), None)
    if not prod:
        print("Producto no encontrado.")
        return
    if cantidad > prod["stok"]:
        print("Stock insuficiente.")
        return

    total = prod["precio"] * cantidad
    total_neto = total - (total * descuento / 100)
    ventas.append({
        "cliente": cliente,
        "tipo_cliente": tipo_cliente,
        "producto": producto,
        "cantidad": cantidad,
        "descuento": descuento,
        "total": total_neto
    })
    prod["stok"] -= cantidad
    print("Venta registrada correctamente.")

def mostrar_ventas():
    if not ventas:
        print("No hay ventas registradas.")
        return
    print(f'{"CLIENTE":<20}{"TIPO":<15}{"PRODUCTO":<25}{"CANTIDAD":<10}{"DESCUENTO":<10}{"TOTAL":<15}')
    print("-"*100)
    for v in ventas:
        print(f'{v["cliente"]:<20}{v["tipo_cliente"]:<15}{v["producto"]:<25}{v["cantidad"]:<10}{v["descuento"]:<10}{v["total"]:<15}')
