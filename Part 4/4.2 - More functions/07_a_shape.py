# Copy here code of line function from previous exercise and use it in your solution
# Write your solution here
def line(x, y):    
    if y == "":
        print(x*"*")
    else:
        print(x*y[0])
        
# You can test your function by calling it within the following block
def shape(x, letter1, y, letter2):
    count = 1
    county = 1 
    while count <= x:
        line(count, letter1)
        count += 1
    if count > x:
        count -= 1 
        while county <= y:
            line(count, letter2)
            county += 1 
        
if __name__ == "__main__":
    shape(5, "x", 2, "o")
     
