# Crear una clase de tipo autor (clase es un molde)
class Autor:
    #Self hace referencia a s'i
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        
    def agregar_libro(self,titulo):
    #agregar libros a la biblioteca del autor
        self.libros.append(titulo)
        print("libro agregado: ", titulo)
    
    #Eliminar libros del autor   
    def eliminar_libro(self, titulo):
        if titulo in self.libros:
            self.libros.remove(titulo)
            print("libro borrado: ", titulo)
        else:
            print("Este libro no pertenece a este autor")

    def buscar_libro(self, titulo):
        if titulo in self.libros:
            print("Libro encontrado: ", titulo)
        else:
            print("Ese libro no fue encontrado.")

    def mostrar_libros(self):
        if len(self.libros) == 0:
            print("No hay libros en la biblioteca del autor.")
        else:
            print("libros de este autor disponibles: ")
            for libro in self.libros:
                print("-", libro)
    
autor1 = Autor("Bernardo Stamateas")
autor2 = Autor("Roberto Balaguer")
autor1.agregar_libro("Gente Toxica")
autor2.agregar_libro("Harry Nevil")
autor1.agregar_libro("Intoxicados por la fe")
autor2.agregar_libro("El otro principito")
autor2.eliminar_libro("Harry Nevil")
autor1.mostrar_libros()
autor2.mostrar_libros()



