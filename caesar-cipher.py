from assets import alphabet, logo

#Variable for looping while
loop = True

#Logic
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
    print(f"Here's the {cipher_direction}d result: {end_text}")

#Display logo
print(logo)

#Loop for keeping app working till a user types 'no'
while loop:
    #Inputs
    reply = "yes"
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        print(f"The alphabet has only 26 letters. Try again.\n")
    else:
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
        reply = input(f"Type 'yes' if you want to go again. Otherwise, type 'no'\n")
    if reply == "yes":
        loop = True
    else:
        loop = False