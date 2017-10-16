def is_sorted(string):
    """Returns True if string is sorted from least to greatest False otherwise."""
    largest = 0
    for char in string.lower():
        if ord(char) > largest:
            largest = ord(char)
        else:
          return False
    return True

print(is_sorted("abed"))

def funny(asdf):
    print(asdf)

myFunc = funny("first")

print(myFunc)