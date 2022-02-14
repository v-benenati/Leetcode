'''
200. Number of Islands
Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.



'''
import copy
class Solution:
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        islandSets = {(row, col):copy.deepcopy( {(row,col)} ) for row in range(m) for col in range(n)}
        numOfIslands = 0
        for row in range(m):
            for col in range(n):
                
                node = (row, col)
                # if grid[row][col] == "1":
                #     numOfIslands += 1
                
                #check Left
                potentialNode = (row-1, col)
                numOfIslands+=self.checkNode(node, potentialNode, m, n, grid, islandSets)
                #check Right
                potentialNode = (row+1, col)
                numOfIslands+=self.checkNode(node, potentialNode, m, n, grid, islandSets)
                #check Down
                potentialNode = (row, col-1)
                numOfIslands+=self.checkNode(node, potentialNode, m, n, grid, islandSets)
                #check Up
                potentialNode = (row, col+1)
                numOfIslands+=self.checkNode(node, potentialNode, m, n, grid, islandSets)
        
        self.printIslands(islandSets)
        return numOfIslands

                
    def printIslands(self, islandSets):
        for key in islandSets.keys():
            print("Key: {}\n----------------".format(key))
            print("Set {}".format(islandSets[key]))
            print("\n------------")

    def checkNode(self, node, potentialNode, m, n, grid, islandSets):
        potentialNode_row, potentialNode_col = potentialNode
        
        if potentialNode_row < 0 or potentialNode_row > m-1:
            return 0
        if potentialNode_col < 0 or potentialNode_col > n-1:
            return 0
        
        if grid[potentialNode_row][potentialNode_col] == "0":
            print("Return 0")
            return 0
        # print(node)
        # nodeKey = str(node[0])+","+str(node[1])
        # print(type(nodeKey))
        # print(nodeKey)
        if potentialNode not in islandSets[node] and node not in islandSets[potentialNode]:
            print("Adding {} to {}".format(potentialNode, node))
            newSet = islandSets[node].union(islandSets[potentialNode])
            # print("New set is {}".format(newSet))
            islandSets[potentialNode] = newSet
            islandSets[node]=newSet
            return -1
        return 0
        

if __name__ == "__main__":
    grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
    grid0 = [
        ["1", "0"],
        ["1", "0"]
    ]
    sol = Solution()

    # print(sol.numIslands(grid0))
    print(sol.numIslands(grid1))


