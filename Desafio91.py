from random import uniform

temperaturas = []

for i in range(10):
    temperatura = uniform(-10.0, 40.0)
    temperaturas.append(temperatura)

print("Temperaturas generadas:")
print(temperaturas)