estudiantes = {
    "Ana": {"Python", "HTML", "CSS"},
    "Juan": {"Python", "HTML"},
    "María": {"Python", "HTML", "CSS"},
    "Pedro": {"Python"},
    "Lucía": {"HTML", "CSS"}
}

cursos_ofrecidos = {"Python", "HTML", "CSS"}


# Estudiantes que completaron todos los cursos
print("Estudiantes que completaron todos los cursos:")

for estudiante in estudiantes:
    if estudiantes[estudiante] == cursos_ofrecidos:
        print(estudiante)


# Estudiantes que completaron solamente Python
curso = "Python"

print("\nEstudiantes que completaron solamente", curso, ":")

for estudiante in estudiantes:
    if estudiantes[estudiante] == {curso}:
        print(estudiante)