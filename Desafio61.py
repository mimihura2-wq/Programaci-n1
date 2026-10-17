#Herencia múltiple y composición
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_datos(self):
        print("Nombre:", self.nombre)


class Gerente(Empleado):
    def __init__(self, nombre, sector):
        super().__init__(nombre)
        self.sector = sector

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Sector:", self.sector)


class Tecnico(Empleado):
    def __init__(self, nombre, especialidad):
        super().__init__(nombre)
        self.especialidad = especialidad

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Especialidad:", self.especialidad)


class Voluntario(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)


# Clases para la composición
class Administrador:
    def administrar(self):
        print("Realiza tareas administrativas.")


class Mantenimiento:
    def mantener(self):
        print("Realiza tareas de mantenimiento.")


# Gerente con un rol adicional
gerente = Gerente("Ana", "Administración")
gerente.administrador = Administrador()

# Técnico con un rol adicional
tecnico = Tecnico("Carlos", "Informática")
tecnico.mantenimiento = Mantenimiento()

# Voluntario
voluntario = Voluntario("Lucía")


# Mostrar información
gerente.mostrar_datos()
gerente.administrador.administrar()

print()

tecnico.mostrar_datos()
tecnico.mantenimiento.mantener()

print()

voluntario.mostrar_datos()