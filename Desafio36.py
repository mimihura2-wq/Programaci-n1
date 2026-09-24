#formato.py
from colorama import Fore, Style

def rojo(texto):
    return Fore.RED + texto + Style.RESET_ALL

def azul(texto):
    return Fore.BLUE + texto + Style.RESET_ALL

def verde(texto):
    return Fore.GREEN + texto + Style.RESET_ALL

def negrita(texto):
    return Style.BRIGHT + texto + Style.RESET_ALL
#programa.py
from formato import rojo, azul, verde, negrita

print(rojo("MENSAJE DE ERROR"))
print(azul("INFORMACIÓN"))
print(verde("OPERACIÓN CORRECTA"))
print(negrita("TÍTULO"))
