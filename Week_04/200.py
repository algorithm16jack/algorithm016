class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        visited = {}
        count = 0
        m = len(grid)
        n = len(grid[0])
        def dfs(grid, i, j):
            visited[(i, j)] = 1
            if i < 0 or j < 0 or i > m - 1 or j > n - 1:
                return
            elif grid[i][j] == '0':
                return
            else:
                for item in [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]:
                    if not visited.get(item):
                        new_i = item[0]
                        new_j = item[1]
                        dfs(grid, new_i, new_j)

        for i in range(m):
            for j in range(n):
                if not visited.get((i, j)) and grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        
        return count