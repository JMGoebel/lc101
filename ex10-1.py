str = "ThiS is a String with Upper and lower case Letters."
str_list = [letter.lower() for letter in str if letter.isalpha()]
letter_dict = {}

for letter in sorted(str_list):
    if letter.isalpha():
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

for (k,v) in letter_dict.items():
    print(k,v)