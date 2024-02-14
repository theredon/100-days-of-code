alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, cipher_shift):
    cipher_text = ""
    for char in plain_text:
        new_index = alphabet.index(char) + cipher_shift
        if new_index >= len(alphabet):
            new_index -= len(alphabet)
        cipher_text += alphabet[new_index]
    print(f"The encoded text is {cipher_text}")

def decrypt(encrypted_text, cipher_shift):
    plain_text = ""
    for char in encrypted_text:
        new_index = alphabet.index(char) - cipher_shift
        if new_index < 0:
            new_index += len(alphabet)
        plain_text += alphabet[new_index]
    print(f"The decrypted text is {plain_text}")

decrypt(encrypted_text=text, cipher_shift=shift)