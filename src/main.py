from utils.operaciones import *
from datos.biblioteca import libros, categorias

continuar = "s"

while continuar == "s":
    print("\n=== BIBLIOTECA ===")
    print("1. Ver libros disponibles")
    print("2. Buscar libros cortos (menos de 400 páginas)")
    print("3. Ver estadísticas")
    print("4. Agregar categoría")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Libros disponibles:")
        mostrar_disponibles(libros)

    elif opcion == "2":
        print("Libros cortos:")
        buscar_por_paginas(libros, 400)

    elif opcion == "3":
        print(f"Total de libros: {contar_libros(libros)}")
        print(f"Promedio de páginas: {promedio_paginas(libros):.2f}")

    elif opcion == "4":
        nueva_categoria = input("Ingresa la nueva categoría: ")
        agregar_categoria(categorias, nueva_categoria)

    elif opcion == "5":
        print("Hasta luego.")
        continuar = "n"