# Write your solution here
pin = 4321
entry = 0
attempts = 0

while pin != entry:
    entry = int(input())
    attempts = attempts + 1
    if pin != entry:
        print("Wrong")
    elif pin == entry:
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
            break
        elif attempts > 1:
            print(f"Correct! It took you {attempts} attempts")
        break
        

