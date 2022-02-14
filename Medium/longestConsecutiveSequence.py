class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        currMax = 0
        graph = {}
       
        queue = []
        for num in nums:
            graph[num] = False
        
        for node in graph:
            if not graph[node]:
                queue.append(node)
                runningMax = 1
                
            while len(queue) != 0:
                seed = queue.pop(0)
                graph[seed] = True
                if seed+1 in graph and not graph[seed+1]:
                    queue.append(seed+1)
                    runningMax+=1
                if seed-1 in graph and not graph[seed-1]:
                    queue.append(seed-1)
                    runningMax+=1
            currMax = max(runningMax, currMax)
        return currMax
                    
       