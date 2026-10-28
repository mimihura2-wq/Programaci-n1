traducciones = {
    "hello": {
        "es": "hola",
        "fr": "bonjour",
        "pr": "olá",
        "it": "ciao",
        "de": "hallo"
    },
    "world": {
        "es": "mundo",
        "fr": "monde",
        "pr": "mundo",
        "it": "mondo",
        "de": "welt"
    },
    "goodbye": {
        "es": "adiós",
        "fr": "au revoir",
        "pr": "adeus",
        "it": "arrivederci",
        "de": "auf wiedersehen"
    }
}


def traducir(palabra_ingles, idiomas):
    for idioma in idiomas:
        if palabra_ingles in traducciones and idioma in traducciones[palabra_ingles]:
            print(idioma, ":", traducciones[palabra_ingles][idioma])
        else:
            print(idioma, ": Traducción no encontrada")


palabra = input("Ingrese una palabra en inglés: ")

idiomas = ["es", "it", "de"]

traducir(palabra, idiomas)