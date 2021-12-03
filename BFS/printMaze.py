
def printMaze(maze,path=""):
    for x,pos in enumerate(maze[0]):
        if pos == "O": start = x
        
    i = 0   
    k = start
    pos = set()
    for p in path: 
        if(p == "L"):
            k-=1
        elif(p == "R"):
            k+=1
        elif(p == "U"):
            i-=1
        elif p == "D":
            i+=1
        
        pos.add((k,i))
        

    for l,row in enumerate(maze):
        for n,col in enumerate(row):
            if (n,l) in pos:
                print("\u001b[31m+ \u001b[0m",end="")
            else:
                print(col+" ",end="")
        print()
                
        
    
        
    

