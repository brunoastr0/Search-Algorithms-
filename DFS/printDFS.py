
def printMaze(maze,frontier):
    for l,row in enumerate(maze):
        for n,col in enumerate(row):
            if (l,n) in frontier:
                print("\u001b[31m+ \u001b[0m",end="")
            else:
                print(col+" ",end="")
        print()
                
        
    
        
    

