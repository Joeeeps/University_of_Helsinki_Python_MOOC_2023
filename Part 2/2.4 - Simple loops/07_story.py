# Write your solution here
word = input("Please type in a word:")
wordmatch = ""
wordlist = ""
end = False

while word != "end":
    if word == wordmatch:
        print(f"{wordlist}")
        end = True  
        break 
    elif word != wordmatch:
        wordlist += word + " "
        wordmatch = word
        word = input("Please type in a word:")    
else:
    print(f"{wordlist}")
        
