# Write your solution here

string = input("Please type in a string: ")

while string != "":
    value = 1 
    dash = "-"
    print(string)
    while len(string) > value:
        value += 1
        dash += "-"
    print(dash)
    string = input("Please type in a string: ")

