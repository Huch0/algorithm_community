row, col = list(map(int,input().split()))
chessboard = []
result = 64

for i in range(row) :
    chessboard.append(input())

for chessboard_row in range(row-7):
    for chessboard_col in range(col-7):
        
        count_top_B = 0
        count_top_W = 0
        
        for x in range(chessboard_row,chessboard_row+8):
            for y in range(chessboard_col,chessboard_col+8):
                if (x+y) % 2 == 0 :
                    if chessboard[x][y] == "B" : count_top_W += 1
                    elif chessboard[x][y] == "W" : count_top_B += 1
                    
                if (x+y) % 2 == 1 :
                    if chessboard[x][y] == "B" : count_top_B += 1
                    elif chessboard[x][y] == "W" : count_top_W += 1
        
        result = (min(result,count_top_B,count_top_W))
                    
print(result)

