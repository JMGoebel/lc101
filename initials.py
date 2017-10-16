""" initials.py:  Takes users name as input and returns their initials """

def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    initials = fullname[0]

    for index, char in enumerate(fullname):
        if char == ' ':
            initials += fullname[index+1]
    return "The initials of '{}' are {}".format(fullname, initials.upper())

def main():
    """ Entry point """
    name = input("What is your name: ")
    print(get_initials(name))

if __name__ == "__main__":
    main()