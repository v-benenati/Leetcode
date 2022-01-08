class Solution:
    def isPalindrome(self, x: int) -> bool:
        strNum = str(x)
        pointer1 = 0 
        pointer2 = len(strNum)-1

        while pointer1 < pointer2:
            if strNum[pointer1] != strNum[pointer2]:
                return False
            pointer1 += 1
            pointer2 -= 1
        return True
        


if __name__ == "__main__":
    test = Solution()
    x  = 5432345
    print(test.isPalindrome(x))