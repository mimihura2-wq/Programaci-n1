#Biografia() y sobrescritura
class Autor:
    def biografia(self):
        print("Es un autor de libros.")


class Escritor(Autor):
    def biografia(self):
        print("Es un escritor que publica obras literarias.")


# Crear un objeto Escritor
escritor1 = Escritor()

# Acceder al método biografia de Escritor
escritor1.biografia()

# Acceder al método biografia de Autor
super(Escritor, escritor1).biografia()