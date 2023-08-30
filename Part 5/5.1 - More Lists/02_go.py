# Write your solution here
def who_won(game_board:list):
    p1 = 0
    p2 = 0
    
    for row in game_board:
        for value in row:
            if value == 1:
                p1 +=1 
            elif value == 2:
                p2+=1      
    if p1 > p2:
        return 1
    elif p2 > p1:
        return 2
    else:
        return 0 

#0 = empty square
#1 = player 1 piece
#2 = player 2 piece 
#number of pieces on board = winner 


if __name__ == "__main__":
    go = [[1, 2, 1], [2, 2, 1], [2, 1, 0]]
    print(who_won(go)) #list and integer
