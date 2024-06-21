import os
os.system("cls")
import json

biblioteca = []

def agregar_libro():
    os.system("cls")
    print("AGREGAR LIBRO 📖")
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el autor del libro: ")
    anio = input("Ingrese el año del libro: ")
    genero = input("Ingrese género del libro: ")

    libro = {
        "titulo": titulo,
        "autor": autor,
        "anio": anio,
        "genero": genero
    }
   
    biblioteca.append(libro)
    print(f"'{titulo}' -  Agregado!")


def mostrar_libros():
    os.system("cls")
    print("VER LIBROS AGREGADOS 📖")
    if biblioteca:
        for libro in biblioteca:
            print(f"Titulo: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['anio']}, Género: {libro['genero']}")
    else: 
        print("No hay libros para mostrar!")


def buscar_libro():
    os.system("cls")
    print("BUSCAR LIBRO 🔍")
    titulo = input("Ingrese titulo del libro a buscar: ")
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo.lower():
            print(f"Titulo: {libro['titulo']}")
            print(f"Autor: {libro['autor']}")
            print(f"Año: {libro['anio']}")
            print(f"Género: {libro['genero']}")
            return
    print(f"Error! el libro {'titulo'} no se encontro en la lista!")


def actualizar_libro():
    os.system("cls")
    print("ACTUALIZAR INFORMACIÓN ⚙️")
    titulo = input("Ingrese titulo del libro a actualizar: ")
    for libro in biblioteca:
        if libro['titulo'].lower() == titulo.lower():
            new_autor = input(f"Ingrese el nuevo autor del libro - actual: {libro['autor']} - : ")
            new_anio = input(f"Ingrese el nuevo año del libro - actual: {libro['anio']} - : ")
            new_genero = input(f"Ingrese el nuevo género del libro - actual: {libro['genero']} - : ")

            libro['autor'] = new_autor if new_autor else libro['autor']
            libro['anio'] = new_anio if new_anio else libro['anio']
            libro['genero'] = new_genero if new_genero else libro['genero']

            print("libro actualizado!")
            return
    print(f"Error! el libro {'titulo'} no se encontro en la lista!")



def guardar_libro_JSON():
    nombre_archivo = input("Ingrese el nombre del archivo JSON donde desea guardar la lista de libros: ")
    with open(nombre_archivo, 'w') as archivo:
        json.dump(biblioteca, archivo)
    print(f"lista de libros guardada en '{nombre_archivo}' ! ")

def salir():
    print("Hasta pronto!!")
    exit



def validar_opcion(lista_opciones):
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in lista_opciones:
                return opc
            else:
                print("ERROR! opción incorrecta!")
        except:
            print("ERROR! debe ingresar un número entero!")