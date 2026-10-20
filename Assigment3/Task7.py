def make_acronym(phrase):
    words = phrase.split()
    acronym = "".join(word[0].upper() for word in words if word)
    return acronym
print(make_acronym("unidentified foreign object"))
input("Enter your string: ")
