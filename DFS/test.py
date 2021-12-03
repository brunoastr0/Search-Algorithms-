from timeit import timeit
from dfs import DFS
from maze import *

dfs_time = timeit(lambda:DFS(createMaze2()),number=1000)

print(f"DFS: {dfs_time:.3f}")