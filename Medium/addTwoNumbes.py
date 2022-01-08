# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        number1 = []
        number2 = []
        ansList = None
        nextNode = l1
        while nextNode != None:
            number1.append(nextNode.val)
            nextNode = nextNode.next
        
        nextNode = l2
        while nextNode != None:
            number2.append(nextNode.val)
            nextNode = nextNode.next
        
        remainder = 0
        while len(number1) != 0 or len(number2) != 0:
            addend1 = 0
            addend2 = 0
            if len(number1) != 0:
                addend1 = number1.pop(0)
            if len(number2) != 0:
                addend2 = number2.pop(0)
            sum1 = addend1 + addend2
            sum1 = remainder + sum1
            remainder = int(sum1/10)
            sum1 = sum1 - remainder*10
            print(sum1)
            if ansList == None:
                ansList = ListNode(sum1)
                currNode = ansList
            else:
                currNode.next = ListNode(sum1)
                currNode = currNode.next
        
        if remainder != 0:
            currNode.next = ListNode(remainder)
            currNode = currNode.next
            
        return ansList 

if __name__ == "__main__":
    
    # l1 = ListNode(2)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)

    # # l2 = [5,6,4]
    # l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)

    # ans = [7,0,8]

    # l1 = [2,4,9]
    # l2 = [5,6,4,9]

    test = Solution()
    calc_ans = test.addTwoNumbers(l1,l2)
    
    nextNode = calc_ans
    while nextNode != None:
        print(nextNode.val)
        nextNode = nextNode.next