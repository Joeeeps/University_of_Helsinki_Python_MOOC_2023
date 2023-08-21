# Write your solution here
# You can test your function by calling it within the following block
def first_word(sentence):
    return sentence.split()[0] #looks at first entry
def second_word(sentence):
    return sentence.split()[1] #looks at second entry
def last_word(sentence):
    return sentence.split()[-1] #looks at last entry

#the sentence.split function splits the words into individual parts of the list

if __name__ == "__main__": 
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
