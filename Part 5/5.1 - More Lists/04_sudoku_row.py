# Write your solution here
#return True if rows don't have duplicates between 1-9
#return False otherwise

def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    
    # Create a set to store encountered numbers
    numbers = set()
    
    for number in row:
        if number in numbers:
            return False  
        if 1 <= number <= 9:
            numbers.add(number) #add a number to the set() numbers to ensure no duplicates  
    
    return True  # No duplicates found, return True

if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    
    print(row_correct(sudoku, 0))  # False
    print(row_correct(sudoku, 1))  # False

