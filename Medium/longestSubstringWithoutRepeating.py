class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pointer1 = 0
        pointer2 = 1
        maxIndex = len(s)-1
        maxLength = 1
        if maxIndex < 1:
            return len(s)
        
        #optimize later for when it can never beat max
        while pointer1 != maxIndex:
            currLetters = {}
            currLetters[s[pointer1]]=True
            while pointer2 != maxIndex+1 and not (s[pointer2] in currLetters):
                # print(s[pointer2])
                # print(currLetters)
                currLetters[s[pointer2]]=True
                pointer2 += 1
               
            substrLen = pointer2-pointer1
            if pointer2 == pointer1+1:
                if s[pointer2] == s[pointer1]:
                    substrLen = 1 
            if substrLen > maxLength:
                maxLength = substrLen
                # print("New max")
                # print(pointer1)
                # print(pointer2)
            pointer1 += 1
            pointer2 = pointer1 + 1
            
        
        return maxLength
        
if __name__== "__main__":
    test = Solution()
    testStr = "abcabcbb"
    # testStr = "aa"
    # testStr = "ab"
    # testStr = "cdd"
    ans = test.lengthOfLongestSubstring(testStr)
    print(ans)