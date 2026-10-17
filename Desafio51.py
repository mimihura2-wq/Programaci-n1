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


# Función para buscar un libro en la biblioteca
def buscar_libro(biblioteca, titulo):

    for autor in biblioteca:

        for libro in autor.libros:

            if libro.titulo == titulo:
                print("Libro encontrado:", libro.titulo)
                print("Autor:", autor.nombre)
                print("Género:", libro.genero)
                print("ISBN:", libro.isbn)
                return libro

    print("El libro no fue encontrado.")
    return None


# Crear autores
autor1 = Autor("George Orwell")
autor2 = Autor("Gabriel García Márquez")

# Crear libros
libro1 = Libro("1984", "Distopía", "123456")
libro2 = Libro("Rebelión en la granja", "Sátira", "789012")
libro3 = Libro("Cien años de soledad", "Realismo mágico", "345678")

# Agregar libros
autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)

autor2.agregar_libro(libro3)

# Crear la biblioteca
biblioteca = [autor1, autor2]

# Buscar un libro
buscar_libro(biblioteca, "1984")