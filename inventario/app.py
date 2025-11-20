inventario=[]
def crear():
   # inventario = cargar_datos()
    nombre = str(input('INGRESA NOMBRE PRODUCTO'))
    precio = float(input('INGRESA EL PRECIO DEL PRODUCTO'))
    cantidad = int(input('INGRESA LA CANTIDAD DEL PRODUCTO'))

    almacenar={
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    inventario.append(almacenar)
   # guardar_datos(inventario)

#---------------------LEER------------------------------
def leer():
  #  inventario = cargar_datos()
    if inventario == []:
        print('-------------NO HAY PRODUCTOS----------------')
        return
    print(f'{"NOMBRE":<15}{"PRECIO:":<15}{"CANTIDAD":<15}')
    for producto in inventario:
     print(f'{producto["nombre"]:<15}{producto["precio"]:<15}{producto["cantidad"]:<15}')

#---------------------ACTUALIZAR-----------------------------

def actualizar():
   # inventario = cargar_datos()
    buscar= input('INGRESA NOMBRE DEL PRODUCTO A ACTUALIZAR: ')
    for producto in inventario:
        if producto['nombre'] == buscar:
            print(f'PRODUCTO ENCONTRADO: {producto}')
            
            nuevo_nombre = input('INGRESE NOMBRE NUEVO: ')
            nuevo_precio = input('INGRESE PRECIO NUEVO: ')
            nueva_cantidad = input('INGRESE CANTIDAD NUEVA: ')

            if nuevo_nombre:
                producto['nombre'] = nuevo_nombre
            if nuevo_precio:
                producto['precio'] = nuevo_precio
            if nueva_cantidad:
                producto['producto'] = nueva_cantidad
                break
        else:
           # guardar_datos(producto)
            print('USUARIO NO ENCONTRADO')


#---------------------ELIMINAR-----------------------------


def eliminar():
   # inventario = cargar_datos()
    buscar = input('INGRESE EL NOMBRE DEL PRODUCTO A ELIMINAR: ')
    for producto in inventario:
        if producto["nombre"] == buscar:
            print(f'PRODUCTO ENCONTRADO {producto}')
            print('DESEA ELIMINAR EL PRODUCTO?')
            respuesta = input('INGRESE SI O NO').lower()
        if respuesta == "si":
            inventario.remove(producto)
            break
        if respuesta == "no":
            print('SE CANCELO LA ACCIÓN')
            break
        volver = input('PRECIOSA S PARA VOLVER')
        if volver == "s":
            break # esto lo debo quitar
            #main()

    else:
    # guardar_datos(producto)
     print('PRODUCTO NO ENCONTRADO: ')    