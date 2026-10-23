numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

if numero1 == numero2 and numero2 == numero3:
    print("Los tres números son iguales.")

elif numero1 >= numero2 and numero1 >= numero3:
    print("El número mayor es:", numero1)

elif numero2 >= numero1 and numero2 >= numero3:
    print("El número mayor es:", numero2)

else:
    print("El número mayor es:", numero3)