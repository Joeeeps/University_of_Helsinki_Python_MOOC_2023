# Write your solution here
letter1 = input("Give us the first letter:")
letter2 = input("Give us the second letter:")
letter3 = input("Give us the third letter:")

if letter1 == letter2 or letter1 == letter3:
    print(f"The letter in the middle is {letter1}")
elif letter2 == letter3:
    print(f"The letter in the middle is {letter2}")
elif letter1 > letter2:
    if letter1 < letter3:
        print(f"The letter in the middle is {letter1}")
    elif letter1 > letter3:
        if letter2 > letter3:
            print(f"The letter in the middle is {letter2}")
        else:
            print(f"The letter in the middle is {letter3}")
elif letter1 > letter3:
    if letter1 < letter2:
        print(f"The letter in the middle is {letter1}")
    elif letter1 > letter2:
        if letter2 > letter3:
            print(f"The letter in the middle is {letter2}")
        else:
            print(f"The letter in the middle is {letter3}")
elif letter2 > letter3:
    print(f"The letter in the middle is {letter3}")
elif letter2 < letter3: 
    print(f"The letter in the middle is {letter2}")     
