class Libro:
    def __init__(self, titulo, genero, isbn):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.disponible = True

    def mostrar_informacion(self):
        print("Título:", self.titulo)
        print("Género:", self.genero)
        print("ISBN:", self.isbn)

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print("Libro prestado:", self.titulo)
        else:
            print("El libro no está disponible.")

    def devolver(self):
        self.disponible = True
        print("Libro devuelto:", self.titulo)


class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print("Libro agregado:", libro.titulo)

    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print("Libro eliminado:", libro.titulo)
        else:
            print("El libro no pertenece a este autor.")

    def mostrar_libros(self):
        print("Libros de", self.nombre)

        for libro in self.libros:
            print("-", libro.titulo)

    def cantidad_libros(self):
        return len(self.libros)


# Crear un autor
autor1 = Autor("George Orwell")

# Crear libros
libro1 = Libro("1984", "Distopía", "123456")
libro2 = Libro("Rebelión en la granja", "Sátira", "789012")

# Agregar libros al autor
autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)

# Mostrar información de los libros
libro1.mostrar_informacion()

# Prestar un libro
libro1.prestar()

# Intentar prestar nuevamente
libro1.prestar()

# Devolver el libro
libro1.devolver()

# Mostrar libros del autor
autor1.mostrar_libros()

# Mostrar cantidad de libros
print("Cantidad de libros:", autor1.cantidad_libros())