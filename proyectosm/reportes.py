
from datos import ventas, inventario
from collections import Counter

def top_productos(n=3):
    if not ventas:
        print("No hay ventas registradas.")
        return
    cont = Counter(v["producto"] for v in ventas)
    print("Top productos más vendidos:")
    for prod, cant in cont.most_common(n):
        print(f"{prod}: {cant} vendidos")

def ventas_por_marca():
    resumen = {}
    for v in ventas:
        marca = next((p["marca"] for p in inventario if p["nombre"] == v["producto"]), None)
        if marca:
            resumen[marca] = resumen.get(marca, 0) + v["cantidad"]
    print("Ventas por marca:")
    for marca, cantidad in resumen.items():
        print(f"{marca}: {cantidad} vendidos")

def ingresos_totales():
    bruto = sum(next(p["precio"] for p in inventario if p["nombre"] == v["producto"]) * v["cantidad"] for v in ventas)
    neto = sum(v["total"] for v in ventas)
    print(f"Ingreso bruto: {bruto}, ingreso neto: {neto}")
