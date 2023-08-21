word = input("Please type in a word: ")
character = input("Please type in a character: ")

firstloc = word.find(character)

if firstloc >= 0:
    substring = word[firstloc:firstloc+3]
    if len(substring) == 3:
        print(substring)

