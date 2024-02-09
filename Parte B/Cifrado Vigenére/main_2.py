import itertools

def vigenere_decrypt(ciphertext, key, alphabet):
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(ciphertext)):
        if ciphertext[i] in alphabet:
            cipher_char_index = alphabet.index(ciphertext[i])
            key_char_index = alphabet.index(key[i % key_length])
            decrypted_index = (cipher_char_index - key_char_index) % len(alphabet)
            decrypted_text += alphabet[decrypted_index]
        else:
            decrypted_text += ciphertext[i]
    return decrypted_text

def brute_force_vigenere(ciphertext, alphabet, max_key_length):
    results = []
    for key_length in range(1, max_key_length + 1):
        for possible_key in itertools.product(alphabet, repeat=key_length):
            key = ''.join(possible_key)
            decrypted_text = vigenere_decrypt(ciphertext, key, alphabet)
            result = f"Key: {key}\nDecrypted Text: {decrypted_text}\n"
            results.append(result)
            print(result)  # Imprime en la terminal

    return results

# Lee el archivo cifrado
file_path = "./Parte B/Cifrado Vigenére/cipher3.txt"
try:
    with open(file_path, "r") as file:
        ciphertext = file.read().upper()
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"Error: {e}")

# Define el alfabeto
alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Especifica la longitud máxima de la clave a probar
max_key_length = 3

# Intenta romper el cifrado Vigenère por fuerza bruta con claves de hasta 5 caracteres
results = brute_force_vigenere(ciphertext, alphabet, max_key_length)

# Guarda los resultados en un archivo llamado "bdd.txt"
output_file_path = "bdd.txt"
with open(output_file_path, "w") as output_file:
    for result in results:
        output_file.write(result)

print(f"Resultados guardados en '{output_file_path}'.")
