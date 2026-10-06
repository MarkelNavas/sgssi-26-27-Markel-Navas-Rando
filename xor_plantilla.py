def xor_bytes(mensaje, clave):
    """
    Aplica XOR byte a byte entre el mensaje y la clave.
    """

    if len(mensaje) != len(clave):
        raise ValueError("El mensaje y la clave deben tener la misma longitud")

    resultado = bytes(
        m ^ k for m, k in zip(mensaje, clave)
    )

    return resultado


# Datos de prueba
mensaje = b"MENSAJE1"
clave = b"CLAVE1"

# Comprobar longitudes
if len(mensaje) != len(clave):
    print("Error: el mensaje y la clave deben tener la misma longitud")
else:
    # Cifrado
    criptograma = xor_bytes(mensaje, clave)

    # Descifrado
    mensaje_descifrado = xor_bytes(criptograma, clave)

    # Mostrar resultados
    print("Mensaje original:     ", mensaje.hex())
    print("Clave:                ", clave.hex())
    print("Criptograma:          ", criptograma.hex())
    print("Mensaje descifrado:   ", mensaje_descifrado.hex())

    # Comprobar que el descifrado es correcto
    if mensaje_descifrado == mensaje:
        print("\nEl descifrado es correcto")
    else:
        print("\nError en el descifrado")