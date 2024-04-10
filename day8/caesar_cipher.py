alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
length = len(alphabet)
app = True


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        # For spaces and numbers
        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}")


while app:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % len(alphabet)
    caesar(start_text=text, cipher_direction=direction, shift_amount=shift)

    if input("Do you want to continue? Yes or no? ").lower() == "no":
        app = False

print("Thank you for using the program.")
