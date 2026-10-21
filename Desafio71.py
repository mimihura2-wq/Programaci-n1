archivo = None

try:
    archivo = open("texto.txt", "r")

    contenido = archivo.read()

    print("Contenido del archivo:")
    print(contenido)

except FileNotFoundError:
    print("Error: el archivo no existe.")

finally:
    if archivo is not None:
        archivo.close()
        print("Archivo cerrado.")