def descifrado_afin(texto, a, b):
    resultado = ""
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    m = len(alfabeto)
    a_inverso = pow(a, -1, m)

    for caracter in texto:
        if caracter.lower() in alfabeto:
            indice = (a_inverso * (alfabeto.index(caracter.lower()) - b)) % m
            if caracter.isupper():
                resultado += alfabeto[indice].upper()
            else:
                resultado += alfabeto[indice]
        else:
            resultado += caracter
    return resultado

def descifrar_archivo_afin(archivo_entrada, archivo_salida, a, b):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo_entrada:
            texto_cifrado = archivo_entrada.read()
            texto_descifrado = descifrado_afin(texto_cifrado, a, b)

        with open(archivo_salida, 'w', encoding='utf-8') as archivo_salida:
            archivo_salida.write(texto_descifrado)

        print(f'Archivo descifrado exitosamente. Resultado en "{archivo_salida}".')

    except FileNotFoundError:
        print(f'Error: El archivo "{archivo_entrada}" no existe.')

if __name__ == "__main__":
    archivo_entrada_cifrado = "./Problema 1/Cifrado afín/encriptado.txt"
    archivo_salida_descifrado = "./Problema 1/Cifrado afín/desencriptado.txt"
    a = 5
    b = 8
    descifrar_archivo_afin(archivo_entrada_cifrado, archivo_salida_descifrado, a, b)
