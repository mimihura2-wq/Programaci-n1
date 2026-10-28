def contar_palabras(nombre_archivo):
    frecuencias = {}

    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            palabras = linea.lower().split()

            for palabra in palabras:
                if palabra in frecuencias:
                    frecuencias[palabra] += 1
                else:
                    frecuencias[palabra] = 1

    palabras_ordenadas = sorted(
        frecuencias.items(),
        key=lambda elemento: elemento[1],
        reverse=True
    )

    print("Las 5 palabras más comunes son:")

    for palabra, cantidad in palabras_ordenadas[:5]:
        print(palabra, "-", cantidad)


contar_palabras("libros.txt")