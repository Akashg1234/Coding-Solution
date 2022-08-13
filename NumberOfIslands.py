class Solution:
    def dfs(self,visited,grid,r,c,ROWS,COLS):
        
        if r<0 or c<0 or c>=COLS or r>=ROWS or grid[r][c]!='1' or (r,c) in visited:
            return
        
        visited.add((r,c))
        self.dfs(visited,grid,r+1,c,ROWS,COLS)
        self.dfs(visited,grid,r-1,c,ROWS,COLS)
        self.dfs(visited,grid,r,c+1,ROWS,COLS)
        self.dfs(visited,grid,r,c-1,ROWS,COLS)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        no_of_island=0
        visited=set()
        ROWS,COLS = len(grid),len(grid[0])
        
        if not grid:
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j]=='1' and (i,j) not in visited:
                    self.dfs(visited,grid,i,j,ROWS,COLS)
                    no_of_island+=1
                    
        return no_of_island
        
