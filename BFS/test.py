from timeit import timeit
from main import BFS
from maze import *

dfs_time = timeit(lambda:BFS(createMaze2()),number=1000)

print(f"BFS: {dfs_time:.3f}")