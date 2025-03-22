def shift_letter(letter, shift):
    if letter == " ":
        return " "
    else:
        original_pos = ord(letter) - ord('A')
        shifted_pos = (original_pos + shift) % 26
        return chr(ord('A') + shifted_pos)

def caesar_cipher(message, shift):
    result = ''
    for char in message:
        if char == ' ':
            result += ' '
        else:
            shifted = (ord(char) - ord('A') + shift) % 26
            result += chr(ord('A') + shifted)
    return result

#https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/

def shift_by_letter(letter, letter_shift):
    if letter == ' ':
        return ' '
    shift = ord(letter_shift) - ord('A')
    shifted_pos = (ord(letter) - ord('A') + shift) % 26
    return chr(ord('A') + shifted_pos)

def vigenere_cipher(plain_text, key):
   encrypted_text = ''
   key_repeated = (key * (len(plain_text) // len(key))) + key[:len(plain_text) % len(key)]
   for i in range(len(plain_text)):
       if plain_text[i].isalpha():
           shift = ord(key_repeated[i].upper()) - ord('A')
           if plain_text[i].isupper():
               encrypted_text += chr((ord(plain_text[i]) + shift - ord('A')) % 26 + ord('A'))
           else:
               encrypted_text += chr((ord(plain_text[i]) + shift - ord('a')) % 26 + ord('a'))
       else:
           encrypted_text += plain_text[i]
   return encrypted_text

# 4/4
# https://www.geeksforgeeks.org/vigenere-cipher/

def scytale_cipher(message, shift):
    while len(message) % shift != 0:
        message += '_'

    ciphered = ''
    total_rows = len(message) // shift

    for i in range(len(message)):
        row = i // shift
        col = i % shift
        index = row + total_rows * col
        ciphered += message[index]

    return ciphered

def scytale_decipher(message, shift):
    rows = len(message) // shift
    deciphered = [''] * len(message)

    for i in range(len(message)):
        cipher_index = (i % rows) * shift + (i // rows)
        deciphered[i] = message[cipher_index]

    return ''.join(deciphered)
