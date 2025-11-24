
from inventario import mostrar_inventario, agregar_producto, actualizar_producto, eliminar_producto
from ventas import registrar_venta, mostrar_ventas
from reportes import top_productos, ventas_por_marca, ingresos_totales

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar inventario")
        print("2. Agregar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Registrar venta")
        print("6. Mostrar ventas")
        print("7. Reportes")
        print("8. Salir")
        opcion = input("Ingrese opción: ")

        if opcion == "1":
            mostrar_inventario()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            registrar_venta()
        elif opcion == "6":
            mostrar_ventas()
        elif opcion == "7":
            top_productos()
            ventas_por_marca()
            ingresos_totales()
        elif opcion == "8":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
