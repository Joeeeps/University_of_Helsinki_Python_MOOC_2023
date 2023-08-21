# Write your solution here
def spruce(x):
    print("a spruce!")
    row = "*"
    finale = x 
    while x > 0:
        spruce = (" " * x + row)
        print(spruce[1:]) # to make sure left most part is touching border 
        row += "**"
        x -= 1 
    if x <= 1: 
        row = "*"
        spruce = (" " * finale + row)
        print(spruce[1:])
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)
