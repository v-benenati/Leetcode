from enum import Enum
import copy

class Connection(Enum):
    NONE = 0
    VISITED = 1
    PACIFIC = 2
    ATLANTIC = 3
    BOTH = 4

class Solution:
           
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        visited = [copy.deepcopy([Connection.NONE]*n) for i in range(m)]
        
        
        #needToVisit?
        self.dfs([0,3], visited, heights, m, n)
        
        print(visited)
        
        
    def bfs(self, seed, visited, heights, both=[], connection = Connection.VISITED):
        queue  = []
        queue.append(seed)
        
        node_row, node_col = node

        #if true, means both and should add to list
        if updateNode(node, visited, connection):
            both.append(node)
            
    
        currentHeight = heights[node_row][node_col] 
        print("CurrentHeight {}".format(currentHeight))
        # print("Height to Down {}".format(heights[node_row+1][node_col]))
        if node_row < m-1 and currentHeight <= heights[node_row+1][node_col]:
            downNode = [node_row+1, node_col]
            if not hasBeenVisited(downNode, visited, connection):
                toSearch.append(downNode)
        if node_row > 0 and currentHeight <= heights[node_row-1][node_col]:
            upNode = [node_row-1, node_col]
            if not hasBeenVisited(upNode, visited, connection):
                toSearch.append(upNode)
        if node_col < n-1 and currentHeight <= heights[node_row][node_col+1]:
            rightNode = [node_row, node_col+1]
            if not hasBeenVisited(rightNode, visited, connection):
                toSearch.append(rightNode)
        if node_col > 0 and currentHeight <= heights[node_row][node_col-1]:
            leftNode = [node_row, node_col-1]
            if not hasBeenVisited(leftNode, visited, connection):
                toSearch.append(leftNode)
                
        for searchNode in toSearch:
            
        
        #run dfs on each toSearch and update current node with their results
#         for searchNode in toSearch:
#             print("Searching {}".format(searchNode))
#             status = self.dfs(searchNode, visited, heights, m, n)
#             updateNode(node, visited, status)
        
       
        
        return visited[node_row][node_col]
        
#     def dfs(self, node, visited, heights, parentStatus, m, n):
        
#         node_row, node_col = node
        
#         #Add node to visited
#         visited[node_row][node_col] = Connection.VISITED
        
            
        
#         #Can Reach Pacific
#         if node_col == 0 or node_row == 0:
#             self.updateNode(node, visited, Connection.PACIFIC)
#         #Can Reach Atlantic:
#         if node_col == n-1 or node_row == m-1:
#             self.updateNode(node, visited, Connection.ATLANTIC)
        
    
#         currentHeight = heights[node_row][node_col] 
#         print("CurrentHeight {}".format(currentHeight))
#         # print("Height to Down {}".format(heights[node_row+1][node_col]))
#         if node_row < m-1 and currentHeight >= heights[node_row+1][node_col]:
#             if hasBeenVisited(node, visited, )visited[node_row+1][node_col] == Connection.NONE:
#                 print("Searching Down")
#                 searchNode = [node_row+1, node_col]
#                 status = self.dfs(searchNode, visited, heights, m, n)
#                 self.updateNode(node, visited, status)
#         if node_row > 0 and currentHeight >= heights[node_row-1][node_col]:
#             if visited[node_row-1][node_col] == Connection.NONE:
#                 print("Searching Up")
#                 searchNode = [node_row-1, node_col]
#                 status = self.dfs(searchNode, visited, heights, m, n)
#                 self.updateNode(node, visited, status)
#         if node_col < n-1 and currentHeight >= heights[node_row][node_col+1]:
#             if visited[node_row][node_col+1] == Connection.NONE:
#                 print("Searching Right")
#                 searchNode = [node_row, node_col+1]
#                 status = self.dfs(searchNode, visited, heights, m, n)
#                 self.updateNode(node, visited, status)
#         if node_col > 0 and currentHeight >= heights[node_row][node_col-1]:
#             print("Maybe Left")
#             if visited[node_row][node_col-1] == Connection.NONE:
#                 print("Searching Left")
#                 searchNode = [node_row, node_col-1]
#                 status = self.dfs(searchNode, visited, heights, m, n)
#                 self.updateNode(node, visited, status)
        
#         #run dfs on each toSearch and update current node with their results
# #         for searchNode in toSearch:
# #             print("Searching {}".format(searchNode))
# #             status = self.dfs(searchNode, visited, heights, m, n)
# #             updateNode(node, visited, status)
        
       
        
#         return visited[node_row][node_col]
    
    def hasBeenVisited(self, node, visited, connectionType):
        
    
            
    def updateNode(self, node, visited, connectionType):
        node_row, node_col = node
        if connectionType==Connection.ATLANTIC:
            if visited[node_row][node_col] != Connection.PACIFIC:
                visited[node_row][node_col] = Connection.ATLANTIC
            else:
                visited[node_row][node_col] = Connection.BOTH
                return True
        elif connectionType==Connection.PACIFIC:
            if visited[node_row][node_col] != Connection.ATLANTIC:
                visited[node_row][node_col] = Connection.PACIFIC
            else:
                visited[node_row][node_col] = Connection.BOTH
                return True
        else:
            visited[node_row][node_col] = Connection.VISITED
        return False
            
        
        
    