def squared(text, length): #set definition
    
    string = (text*(length**2 //len(text)+1)) 
    #repeat text until it covers square area needed
    #length ** 2 // len(text) + 1 calculates this
    new_string = (string[:length**2])
    #new string made to make sure it matches square tile length
    for index in range(0,length**2, length):
        print(new_string[index:index+length])
#for each step in length it prints a new part of the sub string
# Testing the function
if __name__ == "__main__":
    squared("dog",2)
    squared("dog", 5)

#model example
#def squared(characters, size):
#   i = 0
#   row = ""
#   while i < size * size:
#       if i > 0 and i % size == 0:
#           print(row)
#            row = ""
#       row += characters[i % len(characters)]
#        i += 1
#    print(row)
  
