def factorial(numero):

    if numero < 0:
        raise ValueError("El número no puede ser negativo.")

    if numero > 1000:
        raise OverflowError("El número es demasiado grande.")

    resultado = 1

    for i in range(1, numero + 1):
        resultado = resultado * i

    return resultado


try:
    numero = int(input("Ingrese un número entero positivo: "))

    resultado = factorial(numero)

    print("El factorial es:", resultado)

except ValueError:
    print("Error: debe ingresar un número entero positivo.")

except OverflowError:
    print("Error: el número es demasiado grande para procesar.")