number = int(input("Please type in a number: "))
index = 1

while index <= number:
    if index < number:
        print(index)
        print(number)
    elif index == number: # if index becomes more like on even numbers, this is skipped
        print(index) # to avoid duplicates
    index += 1
    number -= 1
