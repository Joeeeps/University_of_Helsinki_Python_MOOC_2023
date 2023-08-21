# Write your solution here
string = input("Please type in a string: ")
strlength = len(string)

while strlength > 0:
    print(string[strlength-1])
    strlength -= 1 
