'''
57. Insert Interval
Medium

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

 

Constraints:

    0 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 105
    intervals is sorted by starti in ascending order.
    newInterval.length == 2
    0 <= start <= end <= 105



'''
import math
class Solution:
    def insert(self, intervals, newInterval):
        leftInterval = self.findIndex(intervals, newInterval[0])
        rightInterval = self.findIndex(intervals, newInterval[1])
        # print(self.findIndex(intervals, newInterval[0]))
        # print(self.findIndex(intervals, newInterval[1]))

        # print(intervals)
        #first delete the intervals in between that are unneeded
        start = -1
        for i in range(int(leftInterval+1), int(rightInterval)):
            if start == -1:
                start = i
            # print("Removing " + str(i))
            intervals.pop(i)
        leftInterval = self.findIndex(intervals, newInterval[0])
        rightInterval = self.findIndex(intervals, newInterval[1])

        if leftInterval == -1:
            intervals.append(newInterval)
            return intervals

        if math.floor(leftInterval) == leftInterval and math.floor(rightInterval) == rightInterval:
            intervals[leftInterval][1] = intervals[rightInterval][1]
            if leftInterval != rightInterval:
                intervals.pop(rightInterval)

        if math.floor(leftInterval) == leftInterval and math.floor(rightInterval) != rightInterval:
            intervals[leftInterval][1] = newInterval[1]
            

        if math.floor(leftInterval) != leftInterval and math.floor(rightInterval) == rightInterval:
            intervals[rightInterval][0] = newInterval[0]

        if math.floor(leftInterval) != leftInterval and math.floor(rightInterval) != rightInterval:
            print(leftInterval)
            print(rightInterval)
            intervals.insert(math.ceil(leftInterval), newInterval) 
       

        # print(self.findIndex(intervals, newInterval[0]))
        # print(self.findIndex(intervals, newInterval[1]))
        # print(intervals)
        return intervals
        
    def findIndex(self, intervals, point):
        if len(intervals) == 0:
            return -1
        rightIndex = len(intervals)-1
        leftIndex = 0
        ##Base case??
        while rightIndex >= leftIndex:
            
            midIndex = leftIndex+(rightIndex-leftIndex)//2
            
            #go right
            if point > intervals[midIndex][1]:
                leftIndex = midIndex+1
            #go left
            elif point < intervals[midIndex][0]:
                rightIndex = midIndex-1
            elif point >= intervals[midIndex][0] and point <= intervals[midIndex][1]:
                return midIndex
            
            # elif point > intervals[midIndex][0]:
            #     return midIndex

            # #is left interval
            # if point == intervals[midIndex][0]:
            #     return midIndex-0.5

            # #is left interval
            # if point == intervals[midIndex][1]:
            #     return midIndex+0.5
            
            
            
        if point > intervals[midIndex][1]:
            return midIndex+0.5  
        if point < intervals[midIndex][0]:
            return midIndex-0.5  
        return midIndex
            
        # midIndex = len(intervals)//2 
        # leftIndex = midIndex
        # rightIndex = midIndex+1
    

if __name__ == "__main__":
    sol = Solution()
    intervals1 = [[1,3],[6,9]]
    newInterval1 = [2,5]

    intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval2 = [4,8]

    intervals3=[[1,5]]
    newInterval3 =[6,8]

    sol.insert(intervals1, newInterval1)
    print("Second Test")
    print(sol.insert(intervals2, newInterval2))

    print("Third Test")
    print(sol.insert(intervals3, newInterval3))