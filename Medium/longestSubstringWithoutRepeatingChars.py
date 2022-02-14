'''
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

'''




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leftPointer = 0
        rightPointer = 0

        locations = {}

        max = 0
        
        while self.valid(leftPointer, rightPointer, s):
            hadConflict = False
            #this substring has a duplicate
            if s[rightPointer] in locations:
                if locations[s[rightPointer]] < leftPointer:
                    locations[s[rightPointer]] = rightPointer
                else:
                    # print("Update left from: {}".format(leftPointer))
                    max = self.updateMax(leftPointer, rightPointer-1, max)
                    leftPointerBeforeChange = leftPointer
                    leftPointer = locations[s[rightPointer]] + 1
                    # print("Update left to: {}".format(leftPointer))
                    hadConflict = True
               
            
            locations[s[rightPointer]] = rightPointer
            # print(locations)
            rightPointer += 1
        # print("\nEnding")
       
        max = self.updateMax(leftPointer, rightPointer-1, max)
        return max

    def updateMax(self, leftPointer, rightPointer, max):
        # print("Left Pointer: {}".format(leftPointer))
        # print("Right Pointer: {}".format(rightPointer))
        if (rightPointer - leftPointer)+1 > max:
            max = rightPointer - leftPointer +1
        # print("Max: {}".format(max))
        return max

    def valid(self, leftPointer, rightPointer, s):
        if rightPointer >= len(s):
            return False
        else:
            return True
        

            
            


if __name__ == "__main__":
    
    #3
    s1 = "abcabcbb"
    #1
    s2 = "bbbbb"
    #3
    s3 = "pwwkew"
    #2
    s0 = "abba"
    #5
    s4 ="tmmzuxt"

    sol = Solution()

    
    print(sol.lengthOfLongestSubstring(s1))
    print(sol.lengthOfLongestSubstring(s2))
    print(sol.lengthOfLongestSubstring(s3))
    print(sol.lengthOfLongestSubstring(s0))
    print(sol.lengthOfLongestSubstring(s4))
    
    
