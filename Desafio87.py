def buscar_libros_por_autor(nombre_archivo, autor_buscar):
    encontrados = False

    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split(";")

            titulo = partes[0]
            autor = partes[1]

            if autor == autor_buscar:
                print("Libro:", titulo)
                encontrados = True

    if not encontrados:
        print("No se encontraron libros de ese autor.")


buscar_libros_por_autor("libros.txt", "J.R.R. Tolkien")