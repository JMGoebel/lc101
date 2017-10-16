str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."

str = input()

l = list(str)
l_dict = {}
for letter in l:
    if l_dict.get(letter):
        l_dict[letter] += 1
    else:
        l_dict[letter] = 1

for key in l_dict.keys():
    print("{}: {}".format(key, l_dict[key]))