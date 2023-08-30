# Write your solution here
#return True if rows don't have duplicates between 1-9
#return False otherwise

def column_correct(sudoku: list, column_no: int):
    numbers = set()
    
    for row in sudoku:
        number = row[column_no] # this looks at each row and grabs the specified column location for each 
        if 1 <= number <= 9: #rest of code same as sudoku row script 
            if number in numbers:
                return False
            numbers.add(number)  # Write your solution here

#Exercise requirements:
#Check each 9 rows
#Check each 9 cols
#Check 3x3 blocks in grid
#If all contain 1-9 at most once, return True, else false

def sudoku_grid_correct(sudoku: list):
    # Check rows
    for row in sudoku:
        numbers = set()
        for number in row:
            if number in numbers:
                return False
            if 1 <= number <= 9:
                numbers.add(number)

    # Check columns
    for col in range(9): #readjusted code compared to orignal exercise
        numbers = set() 
        for row in sudoku: #go through rows
            number = row[col] #grab column numbers for each row, looping through the range 
            if number in numbers: #check cols are ok per row
                return False
            if 1 <= number <= 9:
                numbers.add(number)

    # Check 3x3 blocks
    for row_start in range(0, 9, 3): #start 0, ends 9, jumps 3 to ensure blocky are ok for rows - each 3x3 row at position 0, 3 and 6 are checked (ends as hits 9)
        for col_start in range(0, 9, 3): #does same but for columns, so each column at position 0, 3 and 6 are checked (for each row nested in above loop)
            numbers = set()
            for i in range(row_start, row_start + 3): 
                for j in range(col_start, col_start + 3):
                    number = sudoku[i][j]
                    if number in numbers:
                        return False
                    if 1 <= number <= 9:
                        numbers.add(number)

    return True

    

if __name__ == "__main__":
    sudoku1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9]]

    print(sudoku_grid_correct(sudoku1))
# Write your solution here

#Exercise requirements:
#Check each 9 rows
#Check each 9 cols
#Check 3x3 blocks in grid
#If all contain 1-9 at most once, return True, else false

def sudoku_grid_correct(sudoku: list):
    # Check rows
    for row in sudoku:
        numbers = set()
        for number in row:
            if number in numbers:
                return False
            if 1 <= number <= 9:
                numbers.add(number)

    # Check columns
    for col in range(9): #readjusted code compared to orignal exercise
        numbers = set() 
        for row in sudoku: #go through rows
            number = row[col] #grab column numbers for each row, looping through the range 
            if number in numbers: #check cols are ok per row
                return False
            if 1 <= number <= 9:
                numbers.add(number)

    # Check 3x3 blocks
    for row_start in range(0, 9, 3): #start 0, ends 9, jumps 3 to ensure blocky are ok for rows - each 3x3 row at position 0, 3 and 6 are checked (ends as hits 9)
        for col_start in range(0, 9, 3): #does same but for columns, so each column at position 0, 3 and 6 are checked (for each row nested in above loop)
            numbers = set()
            for i in range(row_start, row_start + 3): 
                for j in range(col_start, col_start + 3):
                    number = sudoku[i][j]
                    if number in numbers:
                        return False
                    if 1 <= number <= 9:
                        numbers.add(number)

    return True

    

if __name__ == "__main__":
    sudoku1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
  [1, 2, 3, 4, 5, 6, 7, 8, 9]]

    print(sudoku_grid_correct(sudoku1))

    return True  

    
if __name__ == "__main__":
    sudoku = [[9, 0, 0, 0, 8, 0, 3, 0, 0], #exercise had weird error when this line was formatted below, although the script worked identically... 
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]]

    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))
