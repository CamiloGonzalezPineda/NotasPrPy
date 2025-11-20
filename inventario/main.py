from crudcsv.app import crear,leer,actualizar,eliminar
def menu():
    while True:
        print('1.AGREGAR INVENTARIO: ')
        print('2.MOSTRAR INVENTARIO: ')
        print('3.ACTUALIZAR INVENTARIO: ')
        print('4, ELIMINAR PRODUCTO: ')
        print('SALIR')
        opcion = input('INGRESE OPCION: ')

        if opcion == "1":
                crear()
        elif opcion == "2":
                leer()
        elif opcion == "3":
                actualizar()
        elif opcion == "4":
              eliminar()
        elif opcion == "5":
             print('---------HASTA LA PROXIMA--------')
             break    
        else:      
            print('OPCION NO VALIDAD')
 
if __name__ == "__main__":
    menu()