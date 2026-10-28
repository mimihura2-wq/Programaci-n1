from random import sample

participantes = [
    "Ana",
    "Juan",
    "María",
    "Pedro",
    "Lucía",
    "Carlos",
    "Sofía",
    "Martín",
    "Laura",
    "Diego"
]

ganadores = sample(participantes, 3)

print("Los ganadores son:")
print(ganadores)