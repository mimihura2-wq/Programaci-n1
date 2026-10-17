try:
    a = int(input("Ingrese el dividendo: "))
    b = int(input("Ingrese el divisor: "))

    resultado = a / b

    print("Resultado:", resultado)

except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.")

except ValueError:
    print("Error: debe ingresar números enteros.")