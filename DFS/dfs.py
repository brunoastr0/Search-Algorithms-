from maze import createMaze, createMaze2
from findEndDFS import findEnd
from printDFS import printMaze
from validDFS import valid





def DFS(maze):
    
    frontier = []
    explored = []
    dfsPath = {}
    for l,row in enumerate(maze):
            for n,col in enumerate(row):
                if col == 'O':
                    start = (l,n)
                    frontier = [(l,n)]
                    explored = [(l,n)]
                    
    
    while True:
        if findEnd(maze, frontier) != False:
            state,cell = findEnd(maze, frontier)
            break
        path = frontier.pop()
        for d in 'WNSE':
            if d == "E":
                childCell = (path[0],path[1]+1)
            elif d == "N":
                childCell = (path[0]-1,path[1])
            elif d == "W":
                childCell = (path[0],path[1]-1)
            
            elif d == "S":
                childCell = (path[0]+1,path[1])
            
            if(childCell in explored):
                continue
            
            else:
                if(valid(maze,childCell)):
                    frontier.append(childCell)
                    explored.append(childCell)
                    dfsPath[childCell] = path
                    
                    
    fwdPath={} 
    

    while cell != start:
        
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    return fwdPath
    
maze = createMaze2()

dfs = DFS(maze)
#print(dfs)
printMaze(maze,dfs)
        
        

          
        
       
        
