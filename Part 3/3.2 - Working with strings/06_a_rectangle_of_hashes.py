# Write your solution here
width = int(input("Width: "))
height = int(input("Height: "))
hash = "#"
value = 1
heightvalue = 1 

while width > value:
    hash += "#"
    value += 1

print(hash)

while height > heightvalue:
    print(hash)
    heightvalue +=1
