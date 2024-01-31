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

def cifrar_archivo(archivo_entrada, archivo_salida, desplazamiento):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo_entrada:
            texto_original = archivo_entrada.read()
            texto_cifrado = cifrado_cesar(texto_original, desplazamiento)

        with open(archivo_salida, 'w', encoding='utf-8') as archivo_salida:
            archivo_salida.write(texto_cifrado)

        print(f'Archivo cifrado exitosamente. Resultado en "{archivo_salida}".')

    except FileNotFoundError:
        print(f'Error: El archivo "{archivo_entrada}" no existe.')

if __name__ == "__main__":
    archivo_entrada = "./Problema 1/Cifrado Cesar/texto.txt"
    archivo_salida = "./Problema 1/Cifrado Cesar/encriptado.txt"
    desplazamiento = 3

    cifrar_archivo(archivo_entrada, archivo_salida, desplazamiento)
