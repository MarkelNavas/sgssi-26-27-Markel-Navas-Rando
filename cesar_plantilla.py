from langdetect import detect

mensaje = input("Introduce el mensaje cifrado: ")

alfabeto = "abcdefghijklmnopqrstuvwxyz"

for clave in range(26):

    resultado = ""

    for letra in mensaje:

        if letra.lower() in alfabeto:

            posicion = alfabeto.index(letra.lower())

            nueva_posicion = (posicion - clave) % 26

            nueva_letra = alfabeto[nueva_posicion]

            if letra.isupper():
                nueva_letra = nueva_letra.upper()

            resultado += nueva_letra

        else:
            resultado += letra

    try:

        idioma = detect(resultado)

        if idioma == "es":
            print("Clave encontrada:", clave)
            print("Mensaje descifrado:", resultado)

    except:
        pass