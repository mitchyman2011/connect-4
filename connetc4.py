#%matplotlib inline
import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import math
import time
i=0
count=0
def row(column,row,game): 
    for r in range(-(n-1),1):
        r=(-1)*r
        
        if game[r][column]==0:

            return r
    


    
def draw(board):
    for x in range(0,k):
        for y in range(0,n):
            if board[y][x]==0:
                return False
    else:
        return True

def Win(board, player):
    


    # check horizontal spaces
    for y in range(n):
        for x in range(k-3):
            if board[y][x] == player and board[y][x+1] == player and board[y][x+2] == player and board[y][x+3] == player:
                print("hori")
                return True

    # check vertical spaces
    for y in range(n-3):
        for x in range(k):
            if board[y][x] == player and board[y+1][x] == player and board[y+2][x] == player and board[y+3][x] == player:
                print("virt")
                return True


   # check / diagonal spaces
    for x in range(k):
        for y in range(n-3):
            if board[y][x] == player and board[y+1][x-1] == player and board[y+2][x-2] == player and board[y+3][x-3] == player:
                print("diagup")
                return True

    # check \ diagonal spaces
    for x in range(k-3):
        for y in range(n-3):
            if board[y][x] == player and board[y+1][x+1] == player and board[y+2][x+2] == player and board[y+3][x+3] == player:
                print("diagdown")
                return True

    return False
def win_pos(board, player):
    # check horizontal spaces
    for y in range(n):
        for x in range(k-3):
            if board[y][x] == player and board[y][x+1] == player and board[y][x+2] == player and board[y][x+3] == player:
                return True

    # check vertical spaces
    for y in range(n-3):
        for x in range(k):
            if board[y][x] == player and board[y+1][x] == player and board[y+2][x] == player and board[y+3][x] == player:
                return True


   # check / diagonal spaces
    for x in range(k):
        for y in range(n-3):
            if board[y][x] == player and board[y+1][x-1] == player and board[y+2][x-2] == player and board[y+3][x-3] == player:
                return True

    # check \ diagonal spaces
    for x in range(k-3):
        for y in range(n-3):
            if board[y][x] == player and board[y+1][x+1] == player and board[y+2][x+2] == player and board[y+3][x+3] == player:
                return True 

    return False
def col():
    col=int(input("what you want:"))
    if col>k-1 or col<0:
        return("m")
    return(col)
def plank(game_b,rows):#player):
    player=2
    try:
        column_choice=int(col())
        print(column_choice)
        rows=row(column_choice,rows,game_b)
   
    except:
        print("put it in range boi")
        return plank(game_b,row)
   # try:
        #if game_b[0][column_choice]>0:
         #   return(game_b,column_choice,player)
    game_b=gab(game_b,player,rows,column_choice)
    #except:
        #print("we dun goofed")
        #play()
    return(game_b,column_choice,player)       
def terminal(board):
    return win_pos(board,2) or win_pos(board,1) 
def minimax(board, max_play, depth ,alpha,beta,rot):
    if depth==0 or terminal(board):
        
        if terminal(board):
            if win_pos(board,1):
                return(None, 100000)
                
            if win_pos(board, 2):
                return(None, - 10000)
            else:
                print("oh know")
                return (None,0)
        else:
            
            return(None,score_pos(board,1))
    if max_play:
        value=-math.inf
        column=random.randint(0,k-1)
        for col in range(0,k):
            try:
                rows =row(col,rot,board)
                if rows == False:
                    pass
                b_copy=board.copy()
                b_copy=game_board(b_copy,1,rows,col)
                b,new_score=minimax(b_copy,False,depth-1,alpha,beta,rot)
            except:
                
                pass
            if new_score > value:
                value=new_score
                column=col
            alpha=max(alpha,value)
            if alpha>= beta:
                
                break
                    
           
        return column, value
    else:
        value=math.inf
        column=random.randint(0,k-1)
        for col in range(0,k):
            try:
                rows =row(col,rot,board)
                if rows == False:
                    pass
                b_copy=board.copy()
                b_copy=game_board(b_copy,2,rows,col)
                b,new_score=minimax(b_copy,True,depth-1,alpha,beta,rot)
            except:
                
                pass
            if new_score< value:
                value=new_score
                column=col
            beta=min(beta,value)
            if alpha>=beta:
                
                break
                
        return column, value

def score_pos(board,player):
   
    op=2
    center_count=0
    score=0
    l=int(math.ceil((k-1)/2))
    for i in range(0,n-1):
        if board[i][l]==player:
            center_count =center_count+1
           
          
    score = center_count*6
    
        # check horizontal spaces
    for y in range(n):
        for x in range(k-2):
            if board[y][x] == player and board[y][x+1] == player:
                score=score+2

    # check vertical spaces
    for y in range(n-2):
        for x in range(k):
            if board[y][x] == player and board[y+1][x] == player:
                score=score+2


   # check / diagonal spaces
    for x in range(k):
        for y in range(n-2):
            if board[y][x] == player and board[y+1][x-1] == player:
                score=score+2

    # check \ diagonal spaces
    for x in range(k-2):
        for y in range(n-2):
            if board[y][x] == player and board[y+1][x+1] == player:
                score=score+2


         # check horizontal spaces
    for y in range(n):
        for x in range(k-2):
            if board[y][x] == op and board[y][x+1] == op:
                score=score-3

    # check vertical spaces
    for y in range(n-2):
        for x in range(k):
            if board[y][x] == op and board[y+1][x] == op:
                score=score-3


   # check / diagonal spaces
    for x in range(k):
        for y in range(n-2):
            if board[y][x] == op and board[y+1][x-1] == op:
                score=score-3

    # check \ diagonal spaces
    for x in range(k-2):
        for y in range(n-2):
            if board[y][x] == op and board[y+1][x+1] == op:
                score=score-3
    # check horizontal spaces
    for y in range(n):
        for x in range(k-3):
            if board[y][x] == player and board[y][x+1] == player and board[y][x+2] == player:
                score=score+5

    # check vertical spaces
    for y in range(n-3):
        for x in range(k):
            if board[y][x] == player and board[y+1][x] == player and board[y+2][x] == player:
                score=score+5


   # check / diagonal spaces
    for x in range(k):
        for y in range(n-3):
            if board[y][x] == player and board[y+1][x-1] == player and board[y+2][x-2] == player:
                score=score+5

    # check \ diagonal spaces
    for x in range(k-3):
        for y in range(n-3):
            if board[y][x] == player and board[y+1][x+1] == player and board[y+2][x+2] == player:
                score=score+5


         # check horizontal spaces
    for y in range(n):
        for x in range(k-3):
            if board[y][x] == op and board[y][x+1] == op and board[y][x+2] == op:
                score=score-6

    # check vertical spaces
    for y in range(n-3):
        for x in range(k):
            if board[y][x] == op and board[y+1][x] == op and board[y+2][x] == op:
                score=score-6


   # check / diagonal spaces
    for x in range(k):
        for y in range(n-3):
            if board[y][x] == op and board[y+1][x-1] == op and board[y+2][x-2] == op:
                score=score-6

    # check \ diagonal spaces
    for x in range(k-3):
        for y in range(n-3):
            if board[y][x] == op and board[y+1][x+1] == op and board[y+2][x+2] == op:
                score=score-6
      # check horizontal spaces
    for y in range(n):
        for x in range(k-3):
            if board[y][x] == player and board[y][x+1] == player and board[y][x+3] == player:
                score=score+5

    # check vertical spaces
    for y in range(n-3):
        for x in range(k):
            if board[y][x] == player and board[y+1][x] == player and board[y+3][x] == player:
                score=score+5


   # check / diagonal spaces
    for x in range(k):
        for y in range(n-3):
            if board[y][x] == player and board[y+1][x-1] == player and board[y+3][x-3] == player:
                score=score+5

    # check \ diagonal spaces
    for x in range(k-3):
        for y in range(n-3):
            if board[y][x] == player and board[y+1][x+1] == player and board[y+3][x+3] == player:
                score=score+5


         # check horizontal spaces
    for y in range(n):
        for x in range(k-3):
            if board[y][x] == op and board[y][x+1] == op and board[y][x+3] == op:
                score=score-6

    # check vertical spaces
    for y in range(n-3):
        for x in range(k):
            if board[y][x] == op and board[y+1][x] == op and board[y+3][x] == op:
                score=score-6


   # check / diagonal spaces
    for x in range(k):
        for y in range(n-3):
            if board[y][x] == op and board[y+1][x-1] == op and board[y+3][x-3] == op:
                score=score-6

    # check \ diagonal spaces
    for x in range(k-3):
        for y in range(n-3):
            if board[y][x] == op and board[y+1][x+1] == op and board[y+3][x+3] == op:
                score=score-6


    return score
def game_board(game_map, player, row, column):
    
    game_map[row][column] = player

    #plt.matshow(game_map);
    #plt.show()
    #print(game_map)
    return(game_map)
def gab(game_map, player, row, column):
    
    
    game_map[row][column] = player

    plt.matshow(game_map);
    plt.show()
    #print(game_map)
    return(game_map)
x=1
def play():

    while play:
        print("clasic is 6x7 no less than 4 on ether")
        global n
        global k
        try:
            n=int(input("how may rows ya want"))

            k= int(input("how may columns you want"))
        except:
            print("put in a int dick")
            play()
        print("stay between 0 and ",k-1,"or youll lose a go")
        print("you are yellow and Ai is blue good luck my dude")
        if n<=4 or k<=4:
            print("come on mate litsen to me")
            play()
        if n>1000 or k>1000:
            print("i want you to have a good time not wait so smaller number")
            play()
        try:    
            game = np.zeros((n, k))
        except:
            print("put in less numbers you penis head dick!!!!!!!!!!!!!!!")
            play()
        plt.matshow(game);
        plt.show()
        x=1
        i=1
        count=0
        while x==1:
            rot=n-1
            
            
            if i<1:
                current_player=2
                game,column_choice,current_player=plank(game,rot)#,current_player)
                
                i=i+1
                count=count+1
            else:
                current_player=1
                chair=random.randint(0,39)
                if chair==1:
                    print("EZ PZ!!!")
                if chair==35:
                    print("Your Rubbish!!!!!")
                if chair==6:
                    print("im winning with this move", column_choice)
                if chair==14:
                    print("OMG it did somthing")
                if chair==30:
                    print("I could be a random number generator and be better than you!!!")
                time_start = time.clock()
                column,maxscore=minimax(game, True, 7,-math.inf,math.inf,rot)
                
                rows=row(column,rot,game)
                game=gab(game,current_player,rows,column)
                time_elapsed = (time.clock() - time_start)
                print(time_elapsed)
                i=0
                count=count+1

                
            if Win(game, current_player)== True and current_player==2:
                 print("you win ")
                 p()
            if Win(game, current_player)== True and current_player==1:
                print("you lose ")
                p()
            
            if draw(game)==True:
                print("draw")
                p()
            else:
                pass
#asking function
def p():
    a = input("would you like to play dude")
    if a == "yes" or a=="ye":
        play()
    if a=="the player died":
        sys.exit()
    else:
        print("you will never escape")
        play()
#start
p()
