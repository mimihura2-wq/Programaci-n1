class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre


class Bibliotecario(Usuario):
    def __init__(self, nombre, seccion, años_experiencia):
        super().__init__(nombre)
        self.seccion = seccion
        self.años_experiencia = años_experiencia

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Sección:", self.seccion)
        print("Años de experiencia:", self.años_experiencia)


# Crear un bibliotecario
bibliotecario1 = Bibliotecario(
    "María",
    "Literatura",
    10
)

# Mostrar sus datos
bibliotecario1.mostrar_datos()