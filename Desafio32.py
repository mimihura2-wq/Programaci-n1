def es_numero_primo(numero):


    if numero < 2:
        return False


    for i in range(2, numero):
        if numero % i == 0:
            print("no es numero primo")
            return False
    print("es numero primo")
    return True
   
es_numero_primo(14)

def es_numero_primo(numero):


    if numero < 2:
        return False


    for item_numero in range(2, numero):
        if numero % item_numero == 0:
            return False


    return True
   
def contar_numeros_primos(lista_numeros):
    total_numeros_primos = 0
   
    for numero in lista_numeros:
        if es_numero_primo(numero):
            total_numeros_primos += 1
           
    return total_numeros_primos

def es_numero_primo(numero):


    if numero < 2:
        return False


    for item_numero in range(2, numero):
        if numero % item_numero == 0:
            return False


    return True
   
def contar_numeros_primos(lista_numeros):
    total_numeros_primos = 0
   
    for numero in lista_numeros:
        if es_numero_primo(numero):
            total_numeros_primos += 1
           
    return total_numeros_primos
 


def main():
    numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


    cantidad_primos = contar_numeros_primos(numeros)
    print("La lista de numeros es: ", numeros)
    print("El total de numeros primos es: ", cantidad_primos)


main()
