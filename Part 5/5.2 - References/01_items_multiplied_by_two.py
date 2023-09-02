# Write your solution here

def double_items(numbers: list): 
    meow = []
    for i in numbers:
        i = i*2
        meow.append(i)
    return meow
    
if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)
