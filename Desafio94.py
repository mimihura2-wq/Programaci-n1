astronomia = {"Ana", "Juan", "María", "Pedro"}
matematica = {"Juan", "María", "Lucía"}
programacion = {"María", "Pedro", "Lucía", "Carlos"}

# Usuarios que participaron en los tres concursos
todos = astronomia & matematica & programacion

# Usuarios que participaron solamente en Programación
solo_programacion = programacion - astronomia - matematica

# Todos los usuarios que participaron en al menos un concurso
todos_los_usuarios = astronomia | matematica | programacion

print("Participaron en los tres concursos:")
print(todos)

print("\nParticiparon solamente en Programación:")
print(solo_programacion)

print("\nParticiparon en al menos un concurso:")
print(todos_los_usuarios)