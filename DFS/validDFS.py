

def valid(maze, childCell) ->bool:
    #lista = [i for i in frontier]
    i,j = childCell
    
    
    if not(0 <= i < len(maze[0]) and 0 <= j <= len(maze)) or maze[i][j] == "#":
            return False
        
    return True
        