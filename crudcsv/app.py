from crudcsv.crud import CRUD


crud = CRUD()
archivo = "datos.csv"
crud.crear_archivo(archivo)

while True:
    print("\n--- MENU ---")
    print("1. Crear persona")
    print("2. Listar personas")
    print("3. Actualizar persona")
    print("4. Eliminar persona")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        id_creado = crud.crear(archivo, nombre, edad)
        print(f"Persona creada con ID: {id_creado}")

    elif opcion == "2":
        datos = crud.listar(archivo)
        if not datos:
            print("No hay datos")
        else:
            for fila in datos:
                print(f"ID: {fila[0]} | Nombre: {fila[1]} | Edad: {fila[2]}")

    elif opcion == "3":
        buscar = int(input("Ingresa el ID a modificar: "))
        datos = crud.listar(archivo)
        for fila in datos:
            if int(fila[0]) == buscar:
                print(f"ID: {fila[0]} | Nombre: {fila[1]} | Edad: {fila[2]}")
                nuevo_nombre = input("Nuevo nombre: ")
                nueva_edad = input("Nueva edad: ")
                crud.actualizar(
                    archivo,
                    buscar,
                    nuevo_nombre if nuevo_nombre else fila[1],
                    nueva_edad if nueva_edad else fila[2]
                )
                print("Registro actualizado")
                break
        else:
            print("No se encontró el ID")
    elif opcion == "4":
        try:
            id_elim = int(input("Ingresa el ID a eliminar: "))
        except ValueError:
            print("ID inválido")
            continue

        crud.eliminar(archivo, id_elim)


    elif opcion == "5":
            print("Saliendo...")
            break

    else:
        print("Opción no válida")

