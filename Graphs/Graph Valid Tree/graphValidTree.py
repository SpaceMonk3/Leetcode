'''
KEY IDEA:
1. A valid tree is when all nodes are connected to another node
2. Any 2 connected nodes have only 1 path
3. There are no cycles in the graph

APPROACH: DFS + Adjacency List + HashSet
1. Build an Adjacency List, from the edges, for the graph with the help of a Hashmap of Lists
2. Recursive DFS traversal, but with a hashset that keeps track of the visited nodes
3. The hashset is passed into the recursive call each time
4. If a node already exists in hashset - return false. 
5. If no DFS recursive call returns False, AND all nodes are in hashset at the end - return True
'''
from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adjList = defaultdict(list)

        for e in edges:
            adjList[e[0]].append(e[1])
            adjList[e[1]].append(e[0])

        def dfs(n: int, parent: int) -> bool: 
            if n in visited:
                return False
            
            visited.add(n)
            for v in adjList[n]:
                if v != parent:
                    if not dfs(v, n):
                        return False

            return True
        
        return dfs(0, -1) and n == len(visited)



