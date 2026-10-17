class Escritor:
    def __init__(self, nombre, libros):
        self.nombre = nombre
        self.libros = libros

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Libros:", self.libros)


class Academico:
    def __init__(self, universidad, especialidad):
        self.universidad = universidad
        self.especialidad = especialidad

    def mostrar_datos_academicos(self):
        print("Universidad:", self.universidad)
        print("Especialidad:", self.especialidad)


class EscritorAcademico(Escritor, Academico):
    def __init__(self, nombre, libros, universidad, especialidad):
        Escritor.__init__(self, nombre, libros)
        Academico.__init__(self, universidad, especialidad)

    def publicar_articulo(self, titulo):
        print("Artículo académico publicado:", titulo)


# Crear un EscritorAcademico
autor1 = EscritorAcademico(
    "María Pérez",
    ["Introducción a Python", "Programación básica"],
    "Universidad de la República",
    "Informática"
)

# Mostrar información
autor1.mostrar_datos()
autor1.mostrar_datos_academicos()

# Publicar un artículo
autor1.publicar_articulo("La programación como herramienta educativa")