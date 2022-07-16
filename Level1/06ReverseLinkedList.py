# Question: https://leetcode.com/problems/reverse-linked-list/

# Solution 2: Iterative: 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        temp = head
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
      
# Verdict:
# Runtime: 64 ms, faster than 31.66% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.4 MB, less than 93.96% of Python3 online submissions for Reverse Linked List.

# ----------------------------------------------------------------------------------------------------

# Solution 1: Recursive:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        rev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rev
      
# Verdict:
# Runtime: 66 ms, faster than 27.24% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 20.7 MB, less than 9.01% of Python3 online submissions for Reverse Linked List.
