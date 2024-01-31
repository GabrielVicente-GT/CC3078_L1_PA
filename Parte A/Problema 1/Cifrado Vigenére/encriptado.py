def cifrado_vigenere(texto, clave):
    resultado = ""
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    clave_extendida = (clave * (len(texto) // len(clave)) + clave[:len(texto) % len(clave)]).lower()

    for i in range(len(texto)):
        if texto[i].lower() in alfabeto:
            indice_texto = alfabeto.index(texto[i].lower())
            indice_clave = alfabeto.index(clave_extendida[i])
            indice_cifrado = (indice_texto + indice_clave) % len(alfabeto)
            resultado += alfabeto[indice_cifrado] if texto[i].islower() else alfabeto[indice_cifrado].upper()
        else:
            resultado += texto[i]

    return resultado

def cifrar_archivo_vigenere(archivo_entrada, archivo_salida, clave):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as file:
            texto_original = file.read()
            texto_cifrado = cifrado_vigenere(texto_original, clave)

        with open(archivo_salida, 'w', encoding='utf-8') as file:
            file.write(texto_cifrado)

        print(f'Archivo cifrado exitosamente. Resultado en "{archivo_salida}".')

    except FileNotFoundError:
        print(f'Error: El archivo "{archivo_entrada}" no existe.')
    except Exception as e:
        print(f'Error al procesar el archivo: {e}')

if __name__ == "__main__":
    archivo_entrada = "./Problema 1/Cifrado Vigenére/texto.txt"
    archivo_salida = "./Problema 1/Cifrado Vigenére/encriptado.txt"
    clave = "clave"

    cifrar_archivo_vigenere(archivo_entrada, archivo_salida, clave)
