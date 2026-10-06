from collections import Counter

# Alfabeto español
ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Frecuencia aproximada de las letras en español
FRECUENCIA_ESPANOL = list("EAOSNRIDLCTUMPBQVGHYFZJÑXKW")

# ==========================================================
# INTRODUCIR AQUÍ EL MENSAJE CIFRADO
# ==========================================================

mensaje = """
PEGA AQUÍ EL MENSAJE CIFRADO
"""

mensaje = mensaje.upper()


# ==========================================================
# 1. CONTAR FRECUENCIAS
# ==========================================================

frecuencias = Counter(
    letra for letra in mensaje
    if letra in ALFABETO
)

print("Frecuencias:")
for letra, cantidad in frecuencias.most_common():
    print(letra, ":", cantidad)


# ==========================================================
# 2. CREAR MAPEO INICIAL
# ==========================================================

letras_cripto = [
    letra for letra, cantidad in frecuencias.most_common()
]

mapeo = dict(zip(letras_cripto, FRECUENCIA_ESPANOL))

print("\nMapeo inicial:")
print(mapeo)


# ==========================================================
# 3. FUNCIÓN PARA DESCIFRAR
# ==========================================================

def aplicar_mapeo(texto, mapeo):

    resultado = []

    for letra in texto:

        if letra in mapeo:
            resultado.append(mapeo[letra])
        else:
            resultado.append(letra)

    return "".join(resultado)


# ==========================================================
# 4. MOSTRAR PRIMERA PROPUESTA
# ==========================================================

print("\nTexto descifrado:")
print(aplicar_mapeo(mensaje, mapeo))


# ==========================================================
# 5. MODO INTERACTIVO
# ==========================================================

while True:

    print("\n--------------------------------")
    print("Texto actual:")
    print(aplicar_mapeo(mensaje, mapeo))
    print("--------------------------------")

    cifrada = input(
        "\nLetra cifrada (o SALIR): "
    ).upper()

    if cifrada == "SALIR":
        break

    original = input(
        "Letra original: "
    ).upper()

    if cifrada in ALFABETO and original in ALFABETO:

        mapeo[cifrada] = original

        print("Sustitución actualizada.")

    else:

        print("Introduce letras válidas.")