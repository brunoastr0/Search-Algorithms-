from printMaze import printMaze


def findEnd(maze, path="") -> bool:
    for x,pos in enumerate(maze[0]):
        if pos == "O":
            start = x
     
    i = 0   
    k = start
    for p in path: 
        if(p == "L"):
            k-=1
        elif(p == "R"):
            k+=1
        elif(p == "U"):
            i-=1
        elif p == "D":
            i+=1

    if(maze[i][k] == "X"):
        print(f"Found: {path}")
        printMaze(maze,path)
        return True
    return False
                        