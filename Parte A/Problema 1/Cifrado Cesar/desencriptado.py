def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    for caracter in texto:
        if caracter.lower() in alfabeto:
            indice = (alfabeto.index(caracter.lower()) + desplazamiento) % len(alfabeto)
            if caracter.isupper():
                resultado += alfabeto[indice].upper()
            else:
                resultado += alfabeto[indice]
        else:
            resultado += caracter
    return resultado

def descifrado_cesar(texto, desplazamiento):
    return cifrado_cesar(texto, -desplazamiento)

def descifrar_archivo(archivo_entrada, archivo_salida, desplazamiento):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo_entrada:
            texto_cifrado = archivo_entrada.read()
            texto_descifrado = descifrado_cesar(texto_cifrado, desplazamiento)

        with open(archivo_salida, 'w', encoding='utf-8') as archivo_salida:
            archivo_salida.write(texto_descifrado)

        print(f'Archivo descifrado exitosamente. Resultado en "{archivo_salida}".')

    except FileNotFoundError:
        print(f'Error: El archivo "{archivo_entrada}" no existe.')

if __name__ == "__main__":

    archivo_cifrado = "./Problema 1/Cifrado Cesar/encriptado.txt"
    archivo_descifrado = "./Problema 1/Cifrado Cesar/desencriptado.txt"
    desplazamiento = 3

    descifrar_archivo(archivo_cifrado, archivo_descifrado, desplazamiento)
