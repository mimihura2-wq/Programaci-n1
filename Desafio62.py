#Polimorfismo
class Musico:
    def instrumento(self):
        pass


class Guitarrista(Musico):
    def instrumento(self):
        print("Toca la guitarra")


class Baterista(Musico):
    def instrumento(self):
        print("Toca la batería")


# Crear objetos
guitarrista = Guitarrista()
baterista = Baterista()

# Guardar ambos objetos en una misma lista
musicos = [guitarrista, baterista]

# Recorrer la lista y demostrar el polimorfismo
for musico in musicos:
    musico.instrumento()