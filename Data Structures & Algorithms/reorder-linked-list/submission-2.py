# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None

        while second:
            next_ = second.next
            second.next = prev
            prev = second
            second = next_
        
        first = head
        second = prev

        while second:
            next_1 = first.next
            next_2 = second.next
            first.next = second
            second.next = next_1
            first = next_1
            second = next_2
        