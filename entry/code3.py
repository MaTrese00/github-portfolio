# Ceasar cipher - Encryption technique

import string # advance functionality for string -> manipulating the string more easily

def caesar_encrypt(message, key): # caesar encrpt function. message: what we want to encrpyt, 

    shift = key % 26 # key: the number of position to shift down the alphabet to create the encrypted message
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

    encrypted_message = message.lower().translate(cipher) # the encrypted message completed here

    return encrypted_message

def caesar_decrypt(encrypted_message, key): # decrypt function

    shift = 26 - (key % 26)
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]) # reverse function like the last function

    message = encrypted_message.translate(cipher)
    return message

message = "Send the message"
key = 3 # shift by 3 letters 

encrypted_message = caesar_encrypt(message, key)
print(f"Encrypted message: {encrypted_message}")

decrypted_message = caesar_decrypt(encrypted_message, key)
print(f"Decrypted message: {decrypted_message}")