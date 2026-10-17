valores = ["10", "5", "0", "hola"]

for valor in valores:
    try:
        numero = int(valor)
        resultado = 100 / numero
        print("Resultado:", resultado)

    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")

    except ValueError:
        print("Error: el valor no es un número entero.")

    except TypeError:
        print("Error: tipo de dato incorrecto.")