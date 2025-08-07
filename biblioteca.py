#Práctica para aprender a manejar diccionarios e iterar sobre sus items

biblioteca = {}

while True:

    genero = input("introduce genero literario (fin para salir): ")
    if genero == "fin":
        break

    if genero not in biblioteca:
        biblioteca[genero] = {}

    while True:
        libro = input("introduce el título del libro (fin para salir): ")
        if libro == "fin":
            break

        
        autor = input("introduce el autor del libro: ")
        año = input("introduce el año de publicación: ")

        biblioteca[genero][libro] = {
            "autor": autor,
            "año": año
            }
        
#contadores:
contadorLibros = 0
generoConMasLibros = ""
mayorCantidadDeLibros = 0

for genero, libros in biblioteca.items():
    cantidadDeLibros = len(libros)
    if cantidadDeLibros > mayorCantidadDeLibros:
        mayorCantidadDeLibros = cantidadDeLibros
        generoConMasLibros = genero
    print(f"\n===genero===: {genero}\n")


    for libro, datos in libros.items():
        contadorLibros += 1
        print(f"libro: {libro}")
        print(f"autor: {datos['autor']}")
        print(f"año: {datos['año']}\n")

print(f"total de libros en la biblioteca: {contadorLibros}\ngenero con más libros: {generoConMasLibros}\ncantidad de libros en {generoConMasLibros}: {mayorCantidadDeLibros}")



