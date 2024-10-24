# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        current = head
        values = []
        while current:
            values.append(current.val)
            current = current.next
        sorted_values = sorted(values)
        
        result = ListNode()
        current = result
        for val in sorted_values:
            current.next = ListNode(val)
            current = current.next
        return result.next
        
        