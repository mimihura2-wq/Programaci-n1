#Crear una lista
biblioteca = []

def agregar_libro(titulo):
    #agregar a la Biblioteca
    biblioteca.append(titulo)
    print("libro agregado: ", titulo)
    
#Eliminar libros   
def eliminar_libro(titulo):
    if titulo in biblioteca:
        biblioteca.remove(titulo)
        print("libro borrado: ", titulo)
    else:
        print("Este libro no existe en la Biblioteca")

def buscar_libro(titulo):
    if titulo in biblioteca:
        print("Libro encontrado: ", titulo)
    else:
        print("Ese libro no fue encontrado.")

def mostrar_libros():
    if len(biblioteca) == 0:
        print("No hay libros en la biblioteca.")
    else:
        print("libros disponibles: ")
        for libro in biblioteca:
            print("-", libro)
        
    
agregar_libro("Educar Sin Culpas")
agregar_libro("Basta de Tanto")
agregar_libro("50 Sombras de Gray")
agregar_libro("Harry Potter")
buscar_libro("Harry Potter")
eliminar_libro("Basta de Tanto")
mostrar_libros()
print(biblioteca)


