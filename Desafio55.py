class Autor:

    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__libros = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def nacionalidad(self):
        return self.__nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    def agregar_libro(self, libro):
        self.__libros.append(libro)

    def obtener_libros(self):
        return self.__libros


# Función que devuelve los títulos de los libros de un autor
def obtener_titulos(autor):
    libros = autor.obtener_libros()
    return libros


# Crear un autor
autor = Autor("Gabriel García Márquez", "Colombiana")

# Agregar libros
autor.agregar_libro("Cien años de soledad")
autor.agregar_libro("El amor en los tiempos del cólera")
autor.agregar_libro("Crónica de una muerte anunciada")

# Obtener los títulos
titulos = obtener_titulos(autor)

print("Títulos de los libros:")
print(titulos)