#LibroEspecializado
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


class LibroEspecializado(Libro):
    def __init__(self, titulo, autor, campo_estudio, nivel_especializacion):
        super().__init__(titulo, autor)
        self.campo_estudio = campo_estudio
        self.nivel_especializacion = nivel_especializacion


# Crear un libro especializado
libro1 = LibroEspecializado(
    "Python para desarrolladores",
    "Ana Pérez",
    "Programación",
    "Avanzado"
)

# Mostrar los datos
print("Título:", libro1.titulo)
print("Autor:", libro1.autor)
print("Campo de estudio:", libro1.campo_estudio)
print("Nivel de especialización:", libro1.nivel_especializacion)