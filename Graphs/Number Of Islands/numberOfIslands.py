'''
dfs recursive approach.
1. nested for loop to detect any cells with 1
2. everytime 1 is detected call dfs (recursive approach)
3. let dfs detect all adjacent 1s and flip the visited 1s to 0s (sink them so they dont appear in main nested loop again)
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r: int, c: int):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return
        
        count = 0
        for r in range(0, len(grid)):
            for c in range(0, len(grid[r])):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)

        return count

        