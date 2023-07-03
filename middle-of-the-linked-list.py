# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        headNode = head
        secondNode = head
        while secondNode and secondNode.next:
             headNode = headNode.next 
             secondNode = secondNode.next.next
        return headNode
        
