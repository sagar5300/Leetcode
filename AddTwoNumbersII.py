# Problem Link: https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1,s2 = '',''
        while l1 is not None:
            s1 = s1 + str(l1.val)
            l1 = l1.next
        while l2 is not None:
            s2 = s2 + str(l2.val)
            l2 = l2.next
        total = str(int(s1[::-1])+int(s2[::-1]))
        tot = total[::-1]
        previousNode = None
        first = None
        for i in tot:
            currentNode = ListNode(i)
            if first is None:
                first = currentNode
            if previousNode is not None:
                previousNode.next = currentNode
            previousNode = currentNode
        return first
        
        
