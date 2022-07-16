# Question: https://leetcode.com/problems/merge-two-sorted-lists/

# Solution 2: Iterative
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        tail = head
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail.next = list1 if list1 else list2
        
        return head.next
      
# Verdict:
# Runtime: 84 ms, faster than 7.23% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.8 MB, less than 78.95% of Python3 online submissions for Merge Two Sorted Lists.

# Solution 1: Recursive
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
          
# Verdict:
# Runtime: 65 ms, faster than 34.29% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.9 MB, less than 78.95% of Python3 online submissions for Merge Two Sorted Lists.
