# Question: https://leetcode.com/problems/middle-of-the-linked-list/

# Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
      
# Verdict:
# Runtime: 49 ms, faster than 46.03% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 13.8 MB, less than 55.26% of Python3 online submissions for Middle of the Linked List.
