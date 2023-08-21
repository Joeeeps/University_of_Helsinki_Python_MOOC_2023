# Write your solution here
string = input("Please type in a string:")
strlength = len(string)

if string[strlength-2] == string[1]:
    print(f"The second and the second to last characters are {string[1]}")
elif string[strlength-2] != string[1]:
    print("The second and the second to last characters are different")    
