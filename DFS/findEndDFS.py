from printDFS import printMaze
pos = set()

def findEnd(maze, frontier: list) ->bool:
    lista = [i for i in frontier]
    i,j = lista.pop()
    pos.add((i,j))
    
    if maze[i][j] == "X":
        return True, (i,j)
    
    return False
        