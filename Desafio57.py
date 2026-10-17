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

class Poeta(Autor):
    def __init__(self, nombre, nacionalidad, tipo_poesia):
        super().__init__(nombre, nacionalidad)
        self.tipo_poesia = tipo_poesia

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Nacionalidad:", self.nacionalidad)
        print("Tipo de poesía:", self.tipo_poesia)


# Crear dos objetos Poeta
poeta1 = Poeta("Pablo Neruda", "Chilena", "Lírica")
poeta2 = Poeta("Mario Benedetti", "Uruguaya", "Social")


# Mostrar sus datos
poeta1.mostrar_datos()
print()

poeta2.mostrar_datos()

# Verificar que utilizan atributos heredados de Autor
print()
print("Nombre del poeta 1:", poeta1.nombre)
print("Nacionalidad del poeta 1:", poeta1.nacionalidad)

# Utilizar un setter heredado
poeta1.nombre = "Pablo Neruda"
print("Nombre actualizado:", poeta1.nombre)