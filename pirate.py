''' translate to and from pirate speal '''

PIRATE_DICT = {
    "sir": "matey",
    "hotel": "fleabag inn",
    "student": "swabbie",
    "boy": "matey",
    "madam": "proud beauty",
    "professor": "foul blaggart",
    "restaurant": "galley",
    "your": "yer",
    "excuse": "arr",
    "students": "swabbies",
    "are": "be",
    "lawyer": "foul blaggart",
    "restroom": "th'head",
    "my": "me",
    "hello": "avast",
    "is": "be",
    "man": "matey"
}

text = "hello my man, please excuse your professor to the restroom!"

def translate(text):
    word_list = text.split()
    new_list = []
    for word in word_list:
        if word[-1].isalpha():
            if PIRATE_DICT.get(word):
                new_list.append(PIRATE_DICT[word])
            else:
                new_list.append(word)
        else:
            if PIRATE_DICT.get(word[:-1]):
                new_list.append(PIRATE_DICT[word[:-1]] + word[-1])
            else:
                new_list.append(word)
    return " ".join(new_list)

print(translate(text))

avast me matey, please arr yer foul blaggart to th' head! but got 
avast me matey, please arr yer foul blaggart to the th'head!
