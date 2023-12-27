import art

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def ceacer_cipher_encode(message, shift):

    message_list = [*message]

    for i, letter in enumerate(message_list):
        if letter.lower() not in alphabet:
            continue
        index = alphabet.index(letter.lower()) + shift
        if index >= len(alphabet):
            index = index - len(alphabet)
        message_list[i] = alphabet[index]
    
    return "".join(message_list)


def ceacer_cipher_decode(message, shift):

    message_list = [*message].lower()

    for i, letter in enumerate(message_list):
        if letter.lower() not in alphabet:
            continue
        index = alphabet.index(letter.lower()) - shift
        if index < 0:
            index = index + len(alphabet)
        message_list[i] = alphabet[index]
    
    return "".join(message_list)


print(art.logo)

while True:
    cmd = input("Type 'q' to exit type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if cmd == 'q':
        break

    if cmd == 'encode':
        while True:
            message = input("Type your message:\n")
            shift = int(input("Type the shift number:\n"))
            print(f"Here's the encoded result: {ceacer_cipher_encode(message=message, shift=shift)}")

            go_again = input("Type 'exit' if you want to leave. to continue encoding type anything\n")
            if go_again == 'exit':
                break
    elif cmd == 'decode':
        while True:
            message = input("Type your message:\n")
            shift = int(input("Type the shift number:\n"))
            print(f"Here's the encoded result: {ceacer_cipher_decode(message=message, shift=shift)}")

            go_again = input("Type 'exit' if you want to leave. to continue decoding type anything\n")
            if go_again == 'exit':
                break

