#%matplotlib inline
import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import math
import time
from numba import njit
@njit
def row(column,row,game): 
    for load in range(0,n):
        
        if game[load][column]==0:

            return load
    return (-1)   
def draw(board):
    for x in range(0,k):
        for y in range(0,n):
            if board[y][x]==0:
                return False
    else:
        return True

def Win(board, player):
    for y in range(n):
        for x in range(k):
            if x<=(k-connect):
                o=[]
                t=[]
                l=[]
                for i in range(0,connect):
                    o.append(board[y][x+i]) 
                    t.append(x+i)
                    l.append(y)
                if len(set(o))==1:
                    
                    if o[0]== player:
                        
                        
                        return (True,t,l)
            if y<=(n-connect):
                o=[]
                t=[]
                l=[]
                for i in range(0,connect):
                    o.append(board[y+i][x]) 
                    l.append(y+i)
                    t.append(x)
                    
                
                if len(set(o))==1:
                    
                    
                    if o[0]== player:
                        return (True,t,l)
            if y<=(n-connect) and x<=(k-connect):
                o=[]
                t=[]
                l=[]
                for i in range(0,connect):
                    o.append(board[y+i][x+i]) 
                    t.append(x+i)
                    l.append(y+i)
                if len(set(o))==1:
                    
                    if o[0]== player:
                        return (True,t,l)
            if (connect-1)<=x and y<=(n-connect):
                o=[]
                t=[]
                l=[]
                
                for i in range(0,connect):
                    o.append(board[y+i][x-i]) 
                    t.append(x-i)
                    l.append(y+i)
                if len(set(o))==1:
                    
                    if o[0]== player:
                        
                        
                        return (True,t,l)
    return False,0,0
@njit      
def win_pos(board, player):
    # check horizontal spaces
    for y in range(n):
        for x in range(k):
            if x<=(k-connect):
                if board[y][x] == player and board[y][x+1] == player and board[y][x+2] == player and board[y][x+3] == player:
                    return True

            if y<=(n-connect):
                if board[y][x] == player and board[y+1][x] == player and board[y+2][x] == player and board[y+3][x] == player:
                    
                    return True
                    
            if y<=(n-connect) and x<=(k-connect):
                if board[y][x] == player and board[y+1][x+1] == player and board[y+2][x+2] == player and board[y+3][x+3] == player:
                    print(player,)
                    return True 

   # check / diagonal spaces
    for x in range(k):
        for y in range(n-connect):
            if board[y][x] == player and board[y+1][x-1] == player and board[y+2][x-2] == player and board[y+3][x-3] == player:
                return True
    for x in range(k-connect ):
        for y in range(n):
            if board[y][x] == player and board[y-1][x+1] == player and board[y-2][x+2] == player and board[y-3][x+3] == player:
                print("im going thhrough here")
                return True
    return False
def col():
    col=int(input("what column would you like: "))
    if col>k-1 or col<0:
        return("m")
    return(col)
def plank(game_b,rows,player):
    column_choice=0
    try:
        column_choice=int(col())
    except:
        print("put it in range boi")
        return (game_b,column_choice,"m")   
        
    rows=row(column_choice,rows,game_b)
    if rows == None:
        return (game_b,column_choice,"m")    
    game_b=gab(game_b,player,rows,column_choice)
    return(game_b,column_choice,player)   
@njit    
def terminal(board):
    return win_pos(board,2) or win_pos(board,1) 
@njit
def minimax(board, max_play, depth ,alpha,beta,rot,player,oplayer):
    if depth==0 or terminal(board):
        
        if terminal(board):
            if win_pos(board,player):
                return(None, 100000)
                
            if win_pos(board, oplayer):
                return(None, -10000000)
            else:
                print("oh know")
                return (None,0)
        else:
            
            return(None,score_pos(board,player,oplayer))
    if max_play:
        value=-math.inf
        column=random.randint(0,k-1)
        for col in range(0,k):
            
            #try:
            rows =row(col,rot,board)
            if rows == -1:
                break
            b_copy=board.copy()
            b_copy=game_board(b_copy,1,rows,col)
            b,new_score=minimax(b_copy,False,depth-1,alpha,beta,rot,player,oplayer)
                
            #except:
                
                
            
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
            
            #try:
            rows =row(col,rot,board)
            if rows == -1:
                break
            b_copy=board.copy()
            b_copy=game_board(b_copy,2,rows,col)
            b,new_score=minimax(b_copy,True,depth-1,alpha,beta,rot,player,oplayer)
                
            if new_score< value:
                value=new_score
                column=col
                
            
            beta=min(beta,value)
            if alpha>=beta:
                
               break
                
        return column, value
@njit
def score_pos(board,player,op):
   
    
   
    center_count=0
    score=0
    l=int(math.ceil((k-1)/2))
    for i in range(0,n-1):
        if board[i][l]==player:
            center_count =center_count+1
            score = center_count*10
        if board[i][l]==op:
            score=score-1
    
    
    
        
    for y in range(n):
        for x in range(k):
            # check horizontal spaces
            if x<=(k-2):
                if board[y][x] == player and board[y][x+1] == player:
                    score=score+3
                if board[y][x] == op and board[y][x+1] == op:
                    score=score-3
            if x<=(k-3):
                if board[y][x] == player and board[y][x+1] == player and board[y][x+2] == player:
                    score=score+5
                if board[y][x] == op and board[y][x+1] == op and board[y][x+2] == op:
                    score=score-5
            if x<=(k-4):
                if board[y][x] == player and board[y][x+1] == player and board[y][x+3] == player:
                    score=score+5
                if board[y][x] == player and board[y][x+2] == player and board[y][x+3] == player:
                    score=score+5
                if board[y][x] == op and board[y][x+1] == op and board[y][x+3] == op:
                    score=score-5
                if board[y][x] == op and board[y][x+2] == op and board[y][x+3] == op:
                    
                    score=score-5
            # check vertical spaces
            if y<=(n-2):
                if board[y][x] == player and board[y+1][x] == player:
                    score=score+3
                if board[y][x] == op and board[y+1][x] == op:
                    score=score-3
            if y<=(n-3):
                if board[y][x] == player and board[y+1][x] == player and board[y+2][x] == player:
                    score=score+5
                if board[y][x] == op and board[y+1][x] == op and board[y+2][x] == op:
                    score=score-5
            # check \ diagonal spaces
            if y<=(n-2) and x<=(k-2):
                if board[y][x] == player and board[y-1][x-1] == player:
                    score=score+3
                if board[y][x] == op and board[y-1][x-1] == op:
                    score=score-3
            if y<=(n-3) and x<=(k-3):
                if board[y][x] == player and board[y-1][x-1] == player and board[y-2][x-2] == player:
                    score=score+5    
                if board[y][x] == op and board[y-1][x-1] == op and board[y-2][x-2] == op:
                    score=score-5
            if y<=(n-4) and x<=(k-4):
                if board[y][x] == player and board[y-1][x-1] == player and board[y-3][x-3] == player:
                    score=score+5
                if board[y][x] == player and board[y-2][x-2] == player and board[y-3][x-3] == player:
                    score=score+5
                if board[y][x] == op and board[y-1][x-1] == op and board[y-3][x-3] == op:
                    score=score-5
    for x in range(k):
        for y in range(n-2):
            # check / diagonal spaces
            if board[y][x] == player and board[y+1][x-1] == player:
                score=score+3
            if board[y][x] == op and board[y+1][x-1] == op:
                score=score-3
            if board[y][x] == player and board[y+1][x-1] == player and board[y+2][x-2] == player:
                score=score+5
            if board[y][x] == op and board[y+1][x-1] == op and board[y+2][x-2] == op:
                score=score-5
            if board[y][x] == player and board[y+1][x-1] == player and board[y+3][x-3] == player:
                score=score+5
            if board[y][x] == player and board[y+2][x-2] == player and board[y+3][x-3] == player:
                score=score+5
            if board[y][x] == op and board[y+1][x-1] == op and board[y+3][x-3] == op:
                score=score-10
    
    return score
@njit
def game_board(game_map, player, row, column):
    
    game_map[row][column] = player

    #plt.matshow(game_map);
    #plt.show()
    #print(game_map)
    return(game_map)
def gab(game_map, player, row, column):
    
    
    game_map[row][column] = player
    #print(row)
   
    #print(game_map)
    return(game_map)
def plot(game_map,t,y,l):
    
    for i in range(0,n):
        for j in range(0,k):
            for a in  range(0,total_players+1):
                if game_map[i][j]==a:
                    c=colour[a]
                    plt.plot(j,i,c,t,y,'b-',markersize=10)
    if t==0:
        title=l
    else:
        title="player ",l," wins"
    plt.title(title)
    plt.show()
    return
x=1
def play():

    while play:
        print("clasic is 6x7 no less than 4 on ether")
        global n
        global k
        try:
            n=int(input("how may rows ya want? "))

            k= int(input("how may columns you want? "))
        except:
            print("put in a int dick")
            play()
        try:
           global h_p_c 
           h_p_c=int(input("how many humans(selecting one will be against the AI must be less than 7)"))
           global connect
           connect=int(input("how many connects"))
        except:
            print("Mitchell is a big penis")
            play()
        if connect<=1 or 7<h_p_c:
            print("OMG humans anoy me!")
            play()
        global total_players
        if h_p_c<1:
            print("ai vs ai doesnt really work")
            play()
        if h_p_c==1:
            total_players=h_p_c+1
            print("you're player one, AI is player 2")
        else:
            total_players=h_p_c
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
        for l in range(1,total_players+1):
                    colour_player=colour[l]
                    plt.plot(l,0,colour_player,markersize=10)
        plt.title("The player colours on the x axis")
        plt.show()
        hellow = input("you ready bro")
        print("i dont care what you think your playin")
        x=1
        i=1
        count=0
        if h_p_c<=1:
               
               hellow = input("Would you like to go:\n 1:first,\n 2: second \n 3:random")
               if hellow==1:
                    i=0
               if hellow==2:
                    i=1
               if hellow==3:
                   i=random.ranint(0,1)
               try:
                   print("your yellow and the AI is red goo luck my friend")
                   difficalty=int(input("Pick your difficalty(type in the number):\n 1:easy\n 2:medium\n 3:hard\n 4:Hyper Hard(might be a little slow)\n 5:impossible(it will take to long hahah)\n"))
               except:
                   print("please do it corectly")
                   play()
               if difficalty==1:
                   depth=3
               if difficalty==2:
                   depth=5
               if difficalty==3:
                   depth=7
               if difficalty==4:
                   depth=9
               if difficalty==5:
                   depth=11
                  
        plot(game,0,0,"Let's Start Dude") 
        while x==1:
            rot=n-1
           
            if h_p_c<2:
                
                
                
                if i<1:
                    current_player="m"
                    while  current_player=="m":
                        current_player=2
                        oplayer=1
                        
                        game,column_choice,current_player=plank(game,rot,current_player)
                        #print(column_choice)
                        #rows=row(column_choice,rot,game)
                        #game=gab(game,current_player,rows,column_choice)
                        
                        i=i+1
                        count=count+1
                else:
                    current_player=1
                    oplayer=2
                    rows="m"
                    while rows=="m":
                        time_b=time.time()
                        print(depth)
                        column,maxscore=minimax(game, True, depth,-math.inf,math.inf,rot,current_player,oplayer)
                        
                        chair=random.randint(0,40)
                        if chair==1:
                            print("EZ PZ!!!")
                        if chair==35:
                            print("Your Rubbish!!!!!")
                        if chair==6:
                            print("im winning with this move!!!!!", column)
                        if chair==14:
                            print("OMG it did somthing!!!!!")
                        if chair==30:
                            print("I could be a random number generator and be better than you!!!")
                            
                        rows=row(column,rot,game)
                        
                        game=gab(game,current_player,rows,column)
            
                        time_elapsed = time.time() - time_b
                        print(time_elapsed)
                        i=0
                        count=count+1
                true,t,y=Win(game,current_player)    
                if true== True and current_player==2:
                    plot(game,t,y,"You Win!")
                    print("you win ")
                    start()
                if true== True and current_player==1:
                    plot(game,t,y,"You Lose")
                    print("you lose ")
                    start()
                if draw(game)==True:
                    print("draw")
                    plot(game,0,0,"Draw")
                    start()
                else:
                    plot(game,0,0,"Keep Going")             
            else:
            
                
            
                
               
                for p in range(1,h_p_c+1):
                    current_player = p
                    game,column_choice,current_player=plank(game,rot,current_player)
                    if current_player=="m":
                        print("you miss your go")
                    true,t,y=Win(game,current_player)    
                        
                    if true== True:
                        plot(game,t,y,current_player)
                        print("you win ")
                        start()
                    if draw(game)==True:
                        print("draw")
                        plot(game,0,0,"Draw")
                        start()
                    else:
                         plot(game,0,0,"Keep Going")
#asking function
def start():
    a = input("would you like to play dude ")
    if a == "yes" or a=="ye":
        play()
    if a=="the player died":
        sys.exit()
    else:
        print("you will never escape")
        play()
global colour
colour=["wo",'ro','yo','go','bo','co','mo','ko']
#start
start()
