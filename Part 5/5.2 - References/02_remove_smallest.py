# Write your solution here

def remove_smallest(numbers: list): 
    meow = min(numbers)
    numbers.remove(meow)
    
if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)
   
