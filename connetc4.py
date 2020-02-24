#%matplotlib inline
import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import math
import time
from numba import njit,prange





@njit
def row(column,row,game,n): 
    for load in range(0,n):
        
        if game[load][column]==0:

            return load
    return (-1)   

def draw(board,connect,n,k):
    for x in range(0,k):
        for y in range(0,n):
            if board[y][x]==0:
                return False
    else:
        return True

def Win(board, player,count,connect,n,k):
    
    
    for y in range(count):
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
def win_pos(board, player,count,connect,n,k):
    for y in range(0,n):
        for x in range(0,k):
            if x<=(k-connect):
                o=[np.complex64(x) for x in range(0)]
         
                
                for i in range(0,connect):
                    o.append(board[y][x+i])
                if len(set(o))==1:
                    
                    if o[0]== player:
                        
                        
                        return (True)
            if y<=(n-connect):
                o=[np.complex64(x) for x in range(0)]
                
                for i in range(0,connect):
                    o.append(board[y+i][x]) 
                    
                
                if len(set(o))==1:
                    
                    
                    if o[0]== player:
                        
                        return (True)
            if y<=(n-connect) and x<=(k-connect):
                o=[np.complex64(x) for x in range(0)]
                for i in range(0,connect):
                    o.append(board[y+i][x+i]) 
                    
                if len(set(o))==1:
                    
                    if o[0]== player:
                        return (True)
            if (connect-1)<=x and y<=(n-connect):
                o=[np.complex64(x) for x in range(0)]
                
                for i in range(0,connect):
                    o.append(board[y+i][x-i]) 
                    
                if len(set(o))==1:
                    
                    if o[0]== player:
                        
                        
                        return (True)
    return False
def col(k):
    col=int(input("what column would you like: "))
    if col>k-1 or col<0:
        return("m")
    return(col)
def plank(game_b,rows,player,n):
    column_choice=0
    try:
        column_choice=int(col())
    except:
        print("put it in range boi")
        return (game_b,column_choice,"m")   
        
    rows=row(column_choice,rows,game_b,n)
    if rows == None:
        return (game_b,column_choice,"m")    
    game_b=gab(game_b,player,rows,column_choice)
    return(game_b,column_choice,player)   
@njit    
def terminal(board,player,oplayer,count,connect,n,k):
    return win_pos(board,player,count,connect,n,k) or win_pos(board,oplayer,count,connect,n,k) 

@njit
def minimax(board, max_play, depth ,alpha,beta,rot,player,oplayer,count,l,connect,n,k,total_players):
    
    if depth==0 or terminal(board,player,oplayer,count,connect,n,k):
    
        
        if terminal(board,player,oplayer,count,connect,n,k):
            if win_pos(board,player,count,connect,n,k):
                
                return(None,100000000)
                
            if win_pos(board, oplayer,count,connect,n,k):
                
                return(None, -100000000)
            else:
                print("oh know")
                return (None,0)
        else:
            
            return(None,score_pos(board,player,oplayer,count,connect,n,k))
    if max_play:
        value=-math.inf
        
        
        #column,value=maxi(board, max_play, depth ,alpha,beta,rot,player,oplayer,count,l,connect,n,k,total_players,value) 
        
        for col in prange(0,k):
            
            #try:
            rows =row(col,rot,board,n)
            count=rows+1
            if rows == -1:
                
                continue
            b_copy=board.copy()
            b_copy=game_board(b_copy,player,rows,col)
            b,new_score=minimax(b_copy,False,depth-1,alpha,beta,rot,player,oplayer,count,l,connect,n,k,total_players)
                
            #except:
            
                
            new_score=new_score- 1/depth
            if new_score > value:
                
                value=new_score
                column=col
             
            alpha=max(alpha,value)
            if alpha>= beta:
               
               break
               
        
        return column, value
    if max_play==False:
        oplayer=l
        l=l+1
        if l==player:
            max_play=True
            if l==total_players:
                l=0
        if total_players<l and l!=player:
            l=1
            max_play=False
        if l!=player:
            max_play=False
        value=math.inf
        print(l)
        #column,value=mini(board, max_play, depth ,alpha,beta,rot,player,oplayer,count,l,connect,n,k,total_players,value)    
        
        
        
        for col in prange(0,k):
           
                
            #try:
            rows =row(col,rot,board,n)
            count=rows+1
            if rows == -1:
                
                continue
            b_copy=board.copy()
            b_copy=game_board(b_copy,oplayer,rows,col)
            b,new_score=minimax(b_copy,max_play,depth-1,alpha,beta,rot,player,oplayer,count,l,connect,n,k,total_players)
            
            new_score=new_score+ 1/depth   
           
            if new_score< value:
                value=new_score
                column=col
                
            
            beta=min(beta,value)
            if alpha>=beta:
               
               break
            
        
        return column, value

@njit
def maxi(board, max_play, depth ,alpha,beta,rot,player,oplayer,count,l,connect,n,k,total_players,value):
            for col in prange(0,k):
                
                #try:
                rows =row(col,rot,board,n)
                count=rows+1
                if rows == -1:
                    
                    continue
                b_copy=board.copy()
                b_copy=game_board(b_copy,player,rows,col)
                b,new_score=minimax(b_copy,False,depth-1,alpha,beta,rot,player,oplayer,count,l,connect,n,k,total_players)
                    
                #except:
                
                    
                new_score=new_score- 1/depth
                if new_score > value:
                    
                    value=new_score
                    column=col
                 
                alpha=max(alpha,value)
                if alpha>= beta:
                   
                   break
            return column,value
@njit
def mini(board, max_play, depth ,alpha,beta,rot,player,oplayer,count,l,connect,n,k,total_players,value):
           
        for col in prange(0,k):
           
                
            #try:
            rows =row(col,rot,board,n)
            count=rows+1
            if rows == -1:
                
                continue
            b_copy=board.copy()
            b_copy=game_board(b_copy,oplayer,rows,col)
            b,new_score=minimax(b_copy,max_play,depth-1,alpha,beta,rot,player,oplayer,count,l,connect,n,k,total_players)
            
            new_score=new_score+ 1/depth   
           
            if new_score< value:
                value=new_score
                column=col
                
            
            beta=min(beta,value)
            if alpha>=beta:
               
               break
        return column,value

@njit
def score_pos(board,player,op,count,connect,n,k ):
    
    
    center_count=0
    score=0
    l=int(math.ceil((k-1)/2))
    for i in range(0,n-1):
        if board[i][l]==player:
            
            center_count =center_count+1
            score = center_count*10
        if board[i][l]==op:
            
            score = score-1
        
    
    
        
    for y in range(count):
            for x in range(k):
                if x<=(k-connect):
                    o=[np.complex64(x) for x in range(0)]
                    
                    for i in range(0,(connect-1)):
                        o.append(board[y][x+i])
                        if len(set(o))==1:
                            
                            if o[0]== player:
                                
                                
                                score=score+2*i
                            if o[0]== op:
                                score=score-2*i
                if y<=(n-connect):
                    o=[np.complex64(x) for x in range(0)]
                    
                    for i in range(0,(connect-1)):
                        o.append(board[y+i][x]) 
                        
                    
                        if len(set(o))==1:
                            
                            
                            if o[0]== player:
                                score=score+2*i
                            if o[0]== op:
                                score=score-2*i
                if y<=(n-connect) and x<=(k-connect):
                    o=[np.complex64(x) for x in range(0)]
                    for i in range(0,(connect-1)):
                        o.append(board[y+i][x+i]) 
                        
                        if len(set(o))==1:
                        
                            if o[0]== player:
                                score=score+2*i
                            if o[0]== op:
                                score=score-2*i
                if (connect-1)<=x and y<=(n-connect):
                    o=[np.complex64(x) for x in range(0)]
                    
                    for i in range(0,(connect-1)):
                        o.append(board[y+i][x-i]) 
                        
                        if len(set(o))==1:
                        
                            if o[0]== player:
                                score=score+2*i
                        
                            if o[0]== op:
                                score=score-2*i
  
    
    return score

@njit
def game_board(game_map, player, row, column):
    
    game_map[row][column] = player

    #plt.matshow(game_map);
    #plt.show()
    
    #print(game_map)
    return(game_map)
@njit
def gab(game_map, player, row, column):
    
    
    game_map[row][column] = player
    #print(row)
   
    #print(game_map)
    return(game_map)
def plot(game_map,t,y,l,n,k,total_players):
    
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
def connect_c():
    try:
        
        connect=int(input("how many connects"))
    except:
        print("please enter an integer")
        connect_c()
    return connect
def game_size(connect):
    print("clasic is 6x7 ")
    
    
    try:
        n=int(input("how may rows ya want? "))
        k= int(input("how may columns you want? "))
    except:
        print("please enter an integer")
        game_size() 
    if k<=connect or n<= connect:
        print("you cant play opn that man its to small")
        game_size()
    if n>1000 or k>1000:
            print("i want you to have a good time not wait so smaller number")
            game_size()
    return(n,k)
def hu_pl_c():
    try:
        
        h_p_c=int(input("how many humans(selecting one will be against the AI must be less than 7)"))
    except:
         print("please enter an integer")
         hu_pl_c()
    
    if 7<h_p_c:
        print("I dont have enough colours, i didnt know poeple could have that many friends")
        hu_pl_c()
    return h_p_c
def turnn():
    hellow = int(input("Would you like to go:\n 1:first,\n 2: second \n 3:random"))
   
    if hellow==1:
        turn=0
    if hellow==2:
        turn=1
    if hellow==3:
        turn=random.ranint(0,1)
        
    return(turn)
    
def diff(total_players):
    try:
        difficalty=int(input("Pick your difficalty(type in the number):\n 1:easy\n 2:medium\n 3:hard\n 4:Hyper Hard(might be a little slow)\n 5:impossible(it will take to long hahah)\n"))
    except:
        print("please try again")
        diff()
    if difficalty==1:
        depth=total_players+1
        return depth
    if difficalty==2:
        depth=total_players*2+1
        return depth
    if difficalty==3:
        depth=total_players*3+1
        return depth
    if difficalty==4:
        depth=total_players*4+1
        return depth
    if difficalty==5:
        depth=total_players*5+1
        return depth
    else:
        diff()
    
def PvE(depth,game,turn,connect,h_p_c,n,k,rot,count,ai_c,total_players):
    x=1
    count=1
    while x==1:
        if turn<1:
            count=player(game,count,h_p_c,n,k,rot,total_players,connect)
            turn=turn+1
            
        else:
            count=ai(depth,game,count,total_players,h_p_c,rot,n,k,connect)
           
            turn=0
        
def player(game,count,h_p_c,n,k,rot,total_players,connect):
    if 0<h_p_c:
        for p in range(1,h_p_c+1):
            current_player = p
            game,column_choice,current_player=plank(game,rot,current_player)
            if current_player=="m":
                print("you miss your go")
            if count<n:
                count=count+1
            check_win(game,current_player,count,n,k,total_players,connect)
    
    return count
           
                            
                
                            
def ai(depth,game,count,total_players,h_p_c,rot,n,k,connect):
    for i in range(h_p_c+1,total_players+1):
        current_player=i
        oplayer=1
        if i == total_players:
            l=1
        else:
            l=current_player+1
        rows="m"
        while rows=="m":
            time_b=time.time()
                                
            cut=count
            
            column,maxscore=minimax(game, True, depth,-math.inf,math.inf,rot,current_player,oplayer,count,l,connect,n,k,total_players)
            
            count=cut
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
                                    
            rows=row(column,rot,game,n)
                    
            game=gab(game,current_player,rows,column)
            if count<n:
                count=count+1    
            time_elapsed = time.time() - time_b
            print(time_elapsed)
        check_win(game,current_player,count,n,k,total_players,connect)  
    return count
def check_win(game,current_player,count,n,k,total_players,connect):
    colour_player=["wo",'red','yellow','green','blue','cyan','magenta','black']
    true,t,y=Win(game,current_player,count,connect,n,k)    
                        
    if true== True:
        plot(game,t,y,colour_player[current_player],n,k,total_players)
        print("you win ")
        start()
    if draw(game,connect,n,k)==True:
        print("draw")
        plot(game,0,0,"Draw",n,k,total_players)
        start()
    else:
        plot(game,0,0,"Keep Going",n,k,total_players)
def AI_n(h_p_c):
      try:
        
        ai_c=int(input("how many ai(total of 2 must be less than 7)"))
      except:
          print("you faliure")
          AI_n()
      
      total_players=ai_c+h_p_c
      if 7<total_players:
          print("god you anoy me ")
          AI_n()
      return(ai_c)
def play():

    while play:
        connect=connect_c()
        n,k=game_size(connect)
        h_p_c=hu_pl_c()
        ai_c=AI_n(h_p_c)
        total_players=ai_c+h_p_c
        game = np.zeros((n, k))
       
        for l in range(1,total_players+1):
                    colour_player=colour[l]
                    plt.plot(l,0,colour_player,markersize=10)
        plt.title("The player colours on the x axis")
        plt.show()
        time.sleep(2)
        x=1
        
       
        
        count=1
        
        rot=n-1
        if h_p_c<=1:
               turn=turnn()
               
               depth=diff(total_players)
    
        plot(game,0,0,"Let's Start Dude",n,k,total_players)
        x==1
        while x==1:
            PvE(depth,game,turn,connect,h_p_c,n,k,rot,count,ai_c,total_players)
           
                    
                    
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
