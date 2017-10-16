""" caesar.py:  ... """

def alphabet_position(letter):
    """ Receives a letter and returns is zero based position """
    return ord(letter.lower()) - 97

def rotate_character(char, rot):
    """ Receives a character and returns 'rot' char ahead """
    if char.lower() >= 'a' and char.lower() <= 'z':
        shift = 97 if char > 'Z' else 65
        return chr(((alphabet_position(char) + rot) % 26) + shift)
    return char

def encrypt(text, rot):
    encrypt_text = ""
    for letter in text:
        encrypt_text += rotate_character(letter, int(rot))
    return encrypt_text

def main():
    """ Entry point """
    message = input("Type a message: ")
    rotate = input("Rotate by: ")
    print(encrypt(message, rotate))

if __name__ == "__main__":
    main()
