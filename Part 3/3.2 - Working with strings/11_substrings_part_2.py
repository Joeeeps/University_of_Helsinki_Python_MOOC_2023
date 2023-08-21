# Write your solution here
string = input("Please type in a string:")
end = len(string) 
start = 0

while 0 <= end:
    print(string[len(string)-start:len(string)])
    end -= 1
    start += 1  
    

