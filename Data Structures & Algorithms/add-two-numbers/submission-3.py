# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            
            sumVal = val1 + val2 + carry
            carry = sumVal//10
            digit = sumVal % 10

            current.next = ListNode(digit)
            current = current.next
        
        return dummy.next