def cifrado_afin(texto, a, b):
    resultado = ""
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    m = len(alfabeto)
    for caracter in texto:
        if caracter.lower() in alfabeto:
            indice = (a * alfabeto.index(caracter.lower()) + b) % m
            if caracter.isupper():
                resultado += alfabeto[indice].upper()
            else:
                resultado += alfabeto[indice]
        else:
            resultado += caracter
    return resultado

def cifrar_archivo_afin(archivo_entrada, archivo_salida, a, b):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo_entrada:
            texto_original = archivo_entrada.read()
            texto_cifrado = cifrado_afin(texto_original, a, b)

        with open(archivo_salida, 'w', encoding='utf-8') as archivo_salida:
            archivo_salida.write(texto_cifrado)

        print(f'Archivo cifrado exitosamente. Resultado en "{archivo_salida}".')

    except FileNotFoundError:
        print(f'Error: El archivo "{archivo_entrada}" no existe.')

if __name__ == "__main__":
    archivo_entrada = "./Problema 1/Cifrado afín/texto.txt"
    archivo_salida = "./Problema 1/Cifrado afín/encriptado.txt"
    a = 5
    b = 8
    cifrar_archivo_afin(archivo_entrada, archivo_salida, a, b)
