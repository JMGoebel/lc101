''' vigenere.py '''
from helpers import alphabet_position, rotate_character

def encrypt(text, word):
    ''' encrypts text '''
    encrypted = ''
    count = 0
    for char in text:
        if char.isalpha():
            encrypted += rotate_character(
                char, alphabet_position(word[count % len(word)]))
            count += 1
        else:
            encrypted += char
    return encrypted

def main():
    ''' main entry '''
    from sys import argv
    message = input("Type a message: ")
    encryption_key = argv[1] if len(argv) > 1 and argv[1].isalpha() else input("Encryption key: ")
    print(encrypt(message, encryption_key))

if __name__ == "__main__":
    main()
