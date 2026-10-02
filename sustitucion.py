from collections import Counter

FRECUENCIA_ESPANOL = list("EAOLSNDRUITCPMYQBHGFVJÑZXKW")

mensaje = """
RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.

AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE.
"""

# Convertimos el mensaje a mayúsculas
mensaje = mensaje.upper()

# Contamos las letras
frecuencias = Counter(
    letra for letra in mensaje
    if letra.isalpha()
)

# Mostramos las letras ordenadas
for letra, cantidad in frecuencias.most_common():
    print(letra, ":", cantidad)

# Generamos el mapeo inicial: la letra mas frecuente del criptograma
# se empareja con la letra mas frecuente del castellano, y asi sucesivamente
letras_cripto = [letra for letra, cantidad in frecuencias.most_common()]
mapeo = dict(zip(letras_cripto, FRECUENCIA_ESPANOL))

# Correcciones manuales según el contexto
mapeo['R'] = 'C'
mapeo['I'] = 'O'
mapeo['A'] = 'D'
mapeo['Z'] = 'U'
mapeo['K'] = 'R'
mapeo['C'] = 'I'
mapeo['P'] = 'M'
mapeo['T'] = 'L'
mapeo['U'] = 'G'
mapeo['S'] = 'Q'
mapeo['N'] = 'S'
mapeo['G'] = 'J'
mapeo['F'] = 'X'
mapeo['D'] = 'P'
mapeo['Q'] = 'B'
mapeo['O'] = 'F'
mapeo['M'] = 'H'
mapeo['v'] = 'V'   # la v minúscula del criptograma es la V del texto claro
mapeo['V'] = 'Y'   # la V mayúscula del criptograma es la Y del texto claro

print()
print("Mapeo propuesto:")
print(mapeo)

def aplicar_mapeo(texto, mapeo):
    resultado = []
    for c in texto:
        if c.isalpha():
            resultado.append(mapeo.get(c, c))
        else:
            resultado.append(c)
    return "".join(resultado)

print()
print("Texto descifrado con la propuesta inicial:")
print(aplicar_mapeo(mensaje, mapeo))

# Modo interactivo
while True:
    print("\nTexto descifrado:")
    print(aplicar_mapeo(mensaje, mapeo))

    cifrada = input("\nLetra cifrada (o SALIR): ").upper()

    if cifrada == "SALIR":
        break

    original = input("Letra original: ").upper()

    if len(cifrada) == 1 and len(original) == 1:
        mapeo[cifrada] = original
        print("Sustitución actualizada.")
    else:
        print("Introduce una sola letra.")