from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
should_continue = "yes"

def caeser(plain_text, cipher_shift, shift_direction):
    cipher_text = ""
    if shift_direction == 'decode':
        cipher_shift *= -1
    for char in plain_text:
        if char not in alphabet:
            cipher_text += char
            continue
        new_index = alphabet.index(char) + cipher_shift
        if shift_direction == "decode" and new_index < 0:
            new_index += len(alphabet)
        elif shift_direction == "encode" and new_index >= len(alphabet):
            new_index -= len(alphabet)
        cipher_text += alphabet[new_index]
    
    print(f"The {shift_direction}d text is {cipher_text}")
    
print(logo)

while should_continue == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    
    shift = shift % len(alphabet)

    caeser(plain_text=text, cipher_shift=shift, shift_direction=direction)

    should_continue = (input("Would you like to encode/decode another message? yes or no? "))

print("Goodbye.")