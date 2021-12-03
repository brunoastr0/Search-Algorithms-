# MAIN ALGORITHM
import  queue
from maze import createMaze, createMaze2
from printMaze import printMaze
from valid import valid
from findEnd import findEnd

def BFS(maze):
    nums = queue.Queue()
    nums.put("")
    add = ""
    
    while not findEnd(maze, add): 
        add = nums.get()
        #print(add)
        for j in ["L", "R", "U", "D"]:
            put = add + j          
            if valid(maze, put):
                nums.put(put)


maze  = createMaze2()
BFS(maze)