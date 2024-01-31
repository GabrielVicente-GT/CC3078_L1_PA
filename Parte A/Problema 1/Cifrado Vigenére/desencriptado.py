def descifrar_vigenere(texto, clave):
    resultado = ""
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    clave_extendida = (clave * (len(texto) // len(clave)) + clave[:len(texto) % len(clave)]).lower()

    for i in range(len(texto)):
        if texto[i].lower() in alfabeto:
            indice_texto = alfabeto.index(texto[i].lower())
            indice_clave = alfabeto.index(clave_extendida[i])
            indice_descifrado = (indice_texto - indice_clave) % len(alfabeto)
            resultado += alfabeto[indice_descifrado] if texto[i].islower() else alfabeto[indice_descifrado].upper()
        else:
            resultado += texto[i]

    return resultado

def descifrar_archivo_vigenere(archivo_entrada, archivo_salida, clave):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as file:
            texto_encriptado = file.read()
            texto_descifrado = descifrar_vigenere(texto_encriptado, clave)

        with open(archivo_salida, 'w', encoding='utf-8') as file:
            file.write(texto_descifrado)

        print(f'Archivo descifrado exitosamente. Resultado en "{archivo_salida}".')

    except FileNotFoundError:
        print(f'Error: El archivo "{archivo_entrada}" no existe.')
    except Exception as e:
        print(f'Error al procesar el archivo: {e}')

if __name__ == "__main__":
    archivo_entrada_encriptado = "./Problema 1/Cifrado Vigenére/encriptado.txt"
    archivo_salida_desencriptado = "./Problema 1/Cifrado Vigenére/desencriptado.txt"
    clave = "clave"

    descifrar_archivo_vigenere(archivo_entrada_encriptado, archivo_salida_desencriptado, clave)
