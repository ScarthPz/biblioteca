import os, time
os.system("cls")
from practica_eje_biblioteca import *


while True:
    os.system("cls")
    print("MENÚ BIBLIOTECA")
    print("1. Agregar un libro")
    print("2. Mostrar libros")
    print("3. Buscar libro por titulo")
    print("4. Actualizar información del libro")
    print("5. Guardar libros en un archivo JSON")
    print("6. Salir")

    opc = validar_opcion([1,2,3,4,5,6])


    os.system("cls")
    if opc ==1:
        agregar_libro()
    elif opc ==2:
        mostrar_libros()
    elif opc==3:
        buscar_libro()
    elif opc==4:
        actualizar_libro()
    elif opc==5:
        guardar_libro_JSON()
    else:
        salir()
    time.sleep(2)
