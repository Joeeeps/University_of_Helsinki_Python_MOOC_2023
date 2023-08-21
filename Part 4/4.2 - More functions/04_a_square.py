# Copy here code of line function from previous exercise
# Write your solution here
def line(x, y):    
    if y == "":
        print(x*"*")
    else:
        print(x*y[0])
        
def square(size, character):
    # You should call function line here with proper parameters
    count = size
    while count > 0:
            line(size, character)
            count -= 1 
            
# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(3, "t")
     
