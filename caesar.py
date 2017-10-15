''' caesar.py '''
from helpers import rotate_character

def encrypt(text, rot):
    ''' encrypts text '''
    encrypted = ''
    for char in text:
        encrypted += rotate_character(char, rot)
    return encrypted

def main():
    ''' main entry '''
    from sys import argv
    message = input("Type a message: ")
    rotation = int(argv[1]) if len(argv) > 1 and argv[1].isdigit() else input("Rotate by: ")
    print(encrypt(message, int(rotation)))

if __name__ == "__main__":
    main()
