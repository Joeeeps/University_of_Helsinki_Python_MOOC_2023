#my solution

def chessboard(x):
    counter = x
    if x % 2 != 0:
        while x > 0:
                if x % 2 != 0:  # if even, start with 10
                    print("10" * (counter // 2) + "1")
                    x -= 1                   
                else:  # if odd, start with 01
                    print("01" * (counter // 2) + "0")
                    x -= 1
    elif x % 2 == 0: 
        while x > 0:
                if x % 2 == 0:  # if even, start with 10
                    print("10" * (counter // 2))
                    x -= 1                   
                else:  # if odd, start with 01
                    print("01" * (counter // 2))  
                    x -= 1

# Testing the function
if __name__ == "__main__":
    chessboard(2)
    chessboard(5)

#def chessboard(size): #model solution uses indexing to match the string length to the 'size' column
#     i = 0
#    while i < size:
#        if i % 2 == 0:
#            row = "10"*size
#        else:
#            row = "01"*size
#        # Remove extra characters at the end of the row
#        print(row[0:size])
#        i += 1

 
