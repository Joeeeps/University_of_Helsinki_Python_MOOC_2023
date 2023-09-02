def print_sudoku(sudoku: list):
    r = 0
    for row in sudoku:
        s = 0
        for character in row:
            s += 1
            if character == 0:
                character = "_"  # Replace 0 with "_"
            m = f"{character} "
            if s % 3 == 0 and s < 8:
                m += " "
            print(m, end="")
        print()
        r += 1
        if r % 3 == 0 and r < 8:
            print()


def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    new_list = []
    for r in sudoku:
        new_list.append(r[:]) #replicate list as new_list 
    new_list[row_no][column_no] = number #add numbers to new list instead of original
    return new_list #return new list 
 
if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    
    if grid_copy is not None:
        print("Original:")
        print_sudoku(sudoku)
        print()
        print("Copy:")
        print_sudoku(grid_copy)
    else:
        print("Invalid input for copy_and_add function.")

