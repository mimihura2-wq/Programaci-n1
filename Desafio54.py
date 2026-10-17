class Autor:

    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad

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


# Crear un autor
autor = Autor("Gabriel García Márquez", "Colombiana")

# Obtener los datos
print("Nombre:", autor.nombre)
print("Nacionalidad:", autor.nacionalidad)

# Modificar los datos
autor.nombre = "Julio Cortázar"
autor.nacionalidad = "Argentina"

print("\nDatos modificados:")
print("Nombre:", autor.nombre)
print("Nacionalidad:", autor.nacionalidad)