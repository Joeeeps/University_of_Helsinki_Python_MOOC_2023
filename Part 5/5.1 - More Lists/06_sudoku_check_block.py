# Write your solution here
#if 3x3 block to right and down from given indexes filled in correctly then return true


def block_correct(sudoku: list, row_no: int, column_no: int):

#we need to get the row number, and include 3 values from the row
#sudoku [column, row]
    rows = sudoku[row_no:row_no+3] #we get the three full rows 
    #return rows[2][:3] #testing on how to return first three values

    block = [row[column_no:column_no+3] for row in rows[0:3]] #not sure why i need to go up to 3
    block = [item for sublist in block for item in sublist]
    #take each item from sublists of block, including within each sublist then add to block variable
    
    numbers = set() #now check the set as done in previous exercises
    
    for number in block:
        if number in numbers:
            return False  
        if 1 <= number <= 9:
            numbers.add(number) #add a number to the set() numbers to ensure no duplicates  
    
    return True  # No duplicates found, return True


if __name__ == "__main__":
    sudoku = [[9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]]
    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))
