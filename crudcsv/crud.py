import csv
import os

class CRUD:

    def crear_archivo(self, archivo):
        if not os.path.exists(archivo):
            with open(archivo, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "nombre", "edad"])
    def listar(self, archivo):
        with open(archivo, "r", newline="") as f:
            reader = csv.reader(f)
            filas = list(reader)
        if len(filas) <= 1:
            return []
        return filas[1:]

    def obtener_nuevo_id(self, archivo):
        with open(archivo, "r", newline="") as f:
            filas = list(csv.reader(f))
        if len(filas) <= 1:  # solo encabezado o vacío
            return 1
        ids = [int(fila[0]) for fila in filas[1:]]
        return max(ids) + 1
    
    def crear(self, archivo, nombre, edad):
        id_nuevo = self.obtener_nuevo_id(archivo)
        with open(archivo, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([id_nuevo, nombre, edad])
        return id_nuevo


    def actualizar(self, archivo, id_buscar, nuevo_nombre, nueva_edad):
        with open(archivo, 'r', newline='') as f:
            filas = list(csv.reader(f))

        for fila in filas[1:]:
            if int(fila[0]) == id_buscar:
                fila[1] = nuevo_nombre
                fila[2] = nueva_edad
                break
        else:
            print("No se encontró el ID")
            return

        # Sobrescribir el CSV con los cambios
        with open(archivo, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(filas)
    def eliminar(self, archivo, id_buscar):
        with open(archivo, 'r', newline='') as f:
            filas = list(csv.reader(f))

        filas_nuevas = [filas[0]]  # conservar encabezado

        encontrado = False
        for fila in filas[1:]:
            if int(fila[0]) != id_buscar:
                filas_nuevas.append(fila)
            else:
                encontrado = True

        if not encontrado:
            print("No se encontró el ID")
            return

        # Sobrescribir el CSV con las filas restantes
        with open(archivo, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(filas_nuevas)
        print(f"Registro con ID {id_buscar} eliminado.")
