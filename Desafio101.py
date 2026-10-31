historial = [
    ("01/09/2026", "Ana", "Gripe"),
    ("05/09/2026", "Juan", "Anginas"),
    ("10/09/2026", "Ana", "Alergia"),
    ("15/09/2026", "Pedro", "Gripe"),
    ("20/09/2026", "Ana", "Gripe")
]


# Consultar el historial de un paciente
paciente = input("Ingrese el nombre del paciente: ")

print("\nHistorial de", paciente, ":")

for registro in historial:
    if registro[1] == paciente:
        print("Fecha:", registro[0])
        print("Diagnóstico:", registro[2])


# Contar diagnósticos distintos
diagnosticos = set()

for registro in historial:
    diagnosticos.add(registro[2])

print("\nCantidad de diagnósticos distintos:", len(diagnosticos))
print("Diagnósticos:", diagnosticos)