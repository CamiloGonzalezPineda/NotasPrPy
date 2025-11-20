# Python Learning
imprime tu primer hola mundo
" print('Hola Mundo') "

# Algoritmos 




# variables

# Tipos de datos en python

# Funciones en Python

# Manejo de archivos
para abrir un archivo se usa la funcion open(archivo.txt, modo)
Los modos más comunes son:
r: leer(read).
w: escribir(write). si el archivo existe lo sobreescribe.
a: añadir al final(append).
r+: lectura y escritura
cerrar un archivo: Siempre debemos cerrrar con close() / o menr aun usar la funcion with open() que lo hace automaticamente y evita errorres.

with open("nombres.txt", "w") as archivo:
 for nombre in datos:
  archivo.write(nombre + "\n")


with open("nombres.txt", "r") as archivo:
 contendido = archivo.read()
 print(contendido)

 # leer linea por linea
 with open("nombre.txt", "r") as archivo:
  for linea in archivo:
   print("linea:", linea.strip())

el manejo de archivos en python te permitealmacenar y recuperar información de manera persistente, aplia las posibiliodades de tus programas es el primmer paso a hacia el trabajo con base de datos y formatos más complejos

#Los modulos
permiten organizar y reutilizar funcinalidades

#Una Libreria
Es una coleccion organizada de unno o más modulos, que proporcionan funcionalidades 

# Las excepciones
acen que tu programa sea más seguro y no se denetenga cuando ocurrre un error 

# IMMPORTAR MODULOS
Importar un modulo completo: import math.
Importar funciones especificas: from math import sqrt, pow.
Alias: mport math as m
Modulo Propio: cualquier archivo.py puede actuar como modulo si lo importas en otro archico

ejemplo de importar la fecha import datetime
print('fecha de hoy:', datetime.date.today())

# Execpciones
 while True: # ciclo while para validar que el valor ingresado sea un numero
        try:# validar que el valor ingresado sea numerico
         valor = int(input('INGRESA VALOR: '))# pedimos el valor del producto  
         break # detenemos si cuple la condicion
        except ValueError: # si no cumple la condicion
          print('ERROR: INGRESE UN VALOR NUMERICO VALIDO') # imprime mensaje de error


# json
Qué es JSON?
JSON significa JavaScript Object Notation.
Es un formato de texto para almacenar datos.
Muy usado para intercambiar información entre sistemas.
Es legible por humanos y fácil de usar en programas.
Se parece a los diccionarios de Python: { "clave": "valor" }.

ejemplo:
{
  "id": 1,
  "nombre": "Camilo",
  "apellido": "González",
  "correo": "camilo@email.com"
}
en python esto sería
paciente = {
    "id": 1,
    "nombre": "Camilo",
    "apellido": "González",
    "correo": "camilo@email.com"
}
# ¿Por qué usar JSON en Python?
Para guardar datos de manera persistente (para que no se borren al cerrar el programa).
Para intercambiar datos entre programas, APIs, aplicaciones web, etc.
Para convertir listas o diccionarios de Python en un archivo de texto que puedas guardar o enviar.

# Cómo Python maneja JSON
Python tiene el módulo json para trabajar con archivos y datos JSON.
Funciones más importantes:
Función	Qué hace
json.dump(obj, file)	Convierte un objeto Python (dict o list) a JSON y lo guarda en un archivo.
json.dumps(obj)	Convierte un objeto Python a JSON en forma de cadena (texto).
json.load(file)	Lee un archivo JSON y lo convierte en objeto Python (dict o list).
json.loads(str)	Convierte un string JSON en objeto Python.

# Extrutura de un json

import json
def guardar_pacientes(pacientes):
    with open("patients.json", "w", encoding="utf-8") as f:
        json.dump(pacientes, f, indent=2, ensure_ascii=False)

def cargar_pacientes():
    try:
        with open("patients.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print('No hay pacientes guardados')
        return []


        # CSV
        import csv
import os

ruta_csv = os.path.join('data', 'inventario.csv')
if not os.path.exists('data'):
    os.makedirs('data')

def cargar_datos():
    try:
        with open(ruta_csv, 'r', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            return list(lector)
    except FileNotFoundError:
        return []

def guardar_datos(lista):
    if not lista:
        return
    columnas = lista[0].keys()
    with open(ruta_csv, 'w', newline='', encoding='utf-8') as f:
        escritor = csv.DictWriter(f, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(lista)

# forma corta para recordar



no me permita mas lieas


