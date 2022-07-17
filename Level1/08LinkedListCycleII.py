# Question: https://leetcode.com/problems/linked-list-cycle-ii/

# Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow2 = head
                while slow != slow2:
                    slow = slow.next
                    slow2 = slow2.next
                return slow    
        return None
      
# Verdict:
# Runtime: 92 ms, faster than 31.07% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 17.3 MB, less than 58.31% of Python3 online submissions for Linked List Cycle II
