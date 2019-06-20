def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return alphabet.index(letter.lower())


def rotate_character(letter, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    startPosition = alphabet_position(letter)
    
    new_position = (startPosition + rot)%26
    if letter.isupper():
        return alphabet[new_position].upper()
    else:
        return alphabet[new_position].lower()

def rotate_string(text, rot):
    encrypted = ''
   
    for letter in text:
        if letter == ' ':
            encrypted = encrypted + ' '
        elif letter.isalpha():
               encrypted += rotate_character(letter,rot)
        else:
           encrypted = encrypted + letter

    return encrypted



def main():
    print(rotate_string('Hello, World!', 4))

if __name__ == "__main__":
    main()