torneo_1 = {"Ana", "Juan", "María", "Pedro"}
torneo_2 = {"Juan", "María", "Lucía", "Carlos"}
torneo_3 = {"María", "Lucía", "Carlos", "Sofía"}

# Atletas que participaron en todos los torneos
todos = torneo_1 & torneo_2 & torneo_3

print("Atletas que participaron en todos los torneos:")
print(todos)


# Atletas que participaron exclusivamente en un torneo
solo_torneo_1 = torneo_1 - torneo_2 - torneo_3
solo_torneo_2 = torneo_2 - torneo_1 - torneo_3
solo_torneo_3 = torneo_3 - torneo_1 - torneo_2

print("\nAtletas exclusivos del torneo 1:")
print(solo_torneo_1)

print("\nAtletas exclusivos del torneo 2:")
print(solo_torneo_2)

print("\nAtletas exclusivos del torneo 3:")
print(solo_torneo_3)


# Total de atletas únicos
todos_los_atletas = torneo_1 | torneo_2 | torneo_3

print("\nTotal de atletas únicos:")
print(len(todos_los_atletas))
