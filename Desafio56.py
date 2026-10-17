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


# Función que busca el autor con más libros
def autor_con_mas_libros(autores):

    autor_mayor = autores[0]

    for autor in autores:
        if len(autor.obtener_libros()) > len(autor_mayor.obtener_libros()):
            autor_mayor = autor

    return autor_mayor


# Crear autores
autor1 = Autor("Gabriel García Márquez", "Colombiana")
autor2 = Autor("Julio Cortázar", "Argentina")
autor3 = Autor("Isabel Allende", "Chilena")

# Agregar libros
autor1.agregar_libro("Cien años de soledad")
autor1.agregar_libro("El amor en los tiempos del cólera")
autor1.agregar_libro("Crónica de una muerte anunciada")

autor2.agregar_libro("Rayuela")
autor2.agregar_libro("Bestiario")

autor3.agregar_libro("La casa de los espíritus")
autor3.agregar_libro("Paula")
autor3.agregar_libro("Eva")
autor3.agregar_libro("Inés del alma mía")

# Crear la lista de autores
autores = [autor1, autor2, autor3]

# Buscar el autor con más libros
mayor = autor_con_mas_libros(autores)

print("El autor con más libros es:", mayor.nombre)
print("Cantidad de libros:", len(mayor.obtener_libros()))