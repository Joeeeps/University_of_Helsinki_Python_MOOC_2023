# Write your solution here

def play_turn(game_board: list, x: int, y: int, piece: str):
    if 0 <= x < len(game_board[0]) and 0 <= y < len(game_board) and game_board[y][x] == "": #is choice wtihin range, and is cell empty
        game_board[y][x] = piece
        return True  # Yes
    else:
        return False  # No, piece there already
    
if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", "X"], ["O", "X", ""]]
    print(play_turn(game_board, 2, 1, "O"))  # This should return True
    print(game_board)  # This should show the updated game board

