#Clase como paquetito de variables
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre != "":
            self.__nombre = nuevo_nombre
        else:
            print("El nombre no puede estar vacío.")

    @property
    def nacionalidad(self):
        return self.__nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad):
        if nueva_nacionalidad != "":
            self.__nacionalidad = nueva_nacionalidad
        else:
            print("La nacionalidad no puede estar vacía.")
            
autor = Autor("Roberto Balaguer", "Uruguayo")
print(autor.nombre)
print(autor.nacionalidad)

#Sustituyendo las propiedades de la variable Autor
autor.nombre = "Bernardo Stamateas"
autor.nacionalidad = "Argentino"
print(autor.nombre)
print(autor.nacionalidad)

