# Write your solution here
string = input("Please type in a string:")
end = len(string)

while len(string) <= end:
    print(string[end:])
    end -= 1 

