
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
        
    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print("Libro eliminado:", libro.titulo)
        else:
            print("El libro no pertenece a este autor")

    def mostrar_libros(self):
        print("Libros de", self.nombre)

        for libro in self.libros:
            print("-", libro.titulo)


# Creamos el autor
autor1 = Autor("George Orwell")

# Creamos objetos de tipo Libro
libro1 = Libro("1984", "Distopía", "123456")
libro2 = Libro("Rebelión en la granja", "Sátira", "789012")

# Agregamos los libros al autor
autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)

# Mostramos los libros
autor1.mostrar_libros