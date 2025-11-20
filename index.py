print('Hola Mundo')

import json


# Manejo de archivos
datos = ["Ana","Luis", "Zoe"]
with open("nombres.txt", "w") as archivo:
 for nombre in datos:
  archivo.write(nombre + "\n")


with open("nombres.txt", "r") as archivo:
 contendido = archivo.read()
 print(contendido)

 # leer linea por linea
 with open("nombres.txt", "r") as archivo:
  for linea in archivo:
   print("linea:", linea.strip())

import datetime
print('fecha de hoy:', datetime.date.today())




def guardar(producto):
 with open('ruta', 'r' , encoding='utf-8') as f:
  json.dump(paciente, indent=2, ensure_ascii=False)

  def carga():
   try:
    with open('ruta', 'w', encoding='utf-8') as f:
     json.load(f)
   except FileNotFoundError:
    print('fallo')
    return []
   

   def guardar():
    with open('ruta', 'r' encoding='utf-8') as f:
        json.dump(ru)

#-------------------

