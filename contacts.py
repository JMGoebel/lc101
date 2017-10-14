CONTACTS = {
    "Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
    "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
    "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")
    }

def sort_contacts(contacts):
    sort_list = []
    names = contacts.keys()
    names = sorted(names)
    for name in names:
        sort_list.append((name, contacts[name][0], contacts[name][1]))
    return sort_list
print(sort_contacts(CONTACTS))