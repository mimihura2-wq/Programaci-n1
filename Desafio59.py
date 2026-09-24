class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")


class LibroDigital(Libro):
    def __init__(self, titulo, autor, isbn, formato, tamaño_archivo):
        super().__init__(titulo, autor, isbn)
        self.formato = formato
        self.tamaño_archivo = tamaño_archivo

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Formato: {self.formato}")
        print(f"Tamaño del archivo: {self.tamaño_archivo} MB")


class EBook(LibroDigital):
    def __init__(self, titulo, autor, isbn, formato, tamaño_archivo, enlace_descarga):
        super().__init__(titulo, autor, isbn, formato, tamaño_archivo)
        self.enlace_descarga = enlace_descarga

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Enlace de descarga: {self.enlace_descarga}")


# Crear un objeto LibroDigital
libro_digital = LibroDigital(
    "Python desde cero",
    "Ana Pérez",
    "123456",
    "PDF",
    5
)

# Crear un objeto EBook
ebook = EBook(
    "Aprendiendo Python",
    "Juan López",
    "789012",
    "EPUB",
    3,
    "https://ejemplo.com/descarga"
)

# Mostrar información
print("LIBRO DIGITAL")
libro_digital.mostrar_informacion()

print("\nEBOOK")
ebook.mostrar_informacion()
