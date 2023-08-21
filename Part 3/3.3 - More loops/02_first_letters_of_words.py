sentence = input("Please type in a sentence:")

words = sentence.split() #By default, split() separates the input string at spaces, creating a list of individual words, each stored an element.  

for word in words: #for each element (word) print the first character
    print(word[0])
