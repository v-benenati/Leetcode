'''
338. Counting Bits
Easy

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

 

Constraints:

    0 <= n <= 105

 

Follow up:

    It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
    Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?


'''

class Solution:
    def countBits(self, n: int):
        bitCounts = [0 for _ in range(n+1)]
        
        nextPower = 1
        lastPower = 0
        for index in range(len(bitCounts)-1):
            if index+1 == nextPower:
                lastPower = nextPower
                nextPower = nextPower << 1
                
            bitCounts[index+1] = 1+bitCounts[index+1-lastPower]
             
        return bitCounts

if __name__ == "__main__":
    sol = Solution()

    input1 = 8

    print(sol.countBits(input1))
    print("Expected: \n{}".format([0,1,1,2,1,2,2,3,1]))