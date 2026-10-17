class Autor:

    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)


# Crear un autor
autor = Autor("Gabriel García Márquez")

# Agregar libros
autor.agregar_libro("Cien años de soledad")
autor.agregar_libro("El amor en los tiempos del cólera")

# Mostrar información
print("Autor:", autor.nombre)
print("Libros:", autor.libros)