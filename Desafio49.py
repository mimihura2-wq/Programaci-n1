class Libro:
    def __init__(self, titulo, genero, isbn):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn


class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print("Libro agregado:", libro.titulo)

    def mostrar_libros(self):
        print("Libros de", self.nombre)

        for libro in self.libros:
            print("-", libro.titulo)


# Creamos varios autores
autor1 = Autor("George Orwell")
autor2 = Autor("Gabriel García Márquez")

# Creamos libros
libro1 = Libro("1984", "Distopía", "123456")
libro2 = Libro("Rebelión en la granja", "Sátira", "789012")
libro3 = Libro("Cien años de soledad", "Realismo mágico", "345678")
libro4 = Libro("El amor en los tiempos del cólera", "Romance", "901234")

# Agregamos los libros a sus autores
autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)

autor2.agregar_libro(libro3)
autor2.agregar_libro(libro4)


# Creamos una lista con los autores
biblioteca = [autor1, autor2]


# Mostramos los autores y sus libros
for autor in biblioteca:
    autor.mostrar_libros()
    print()