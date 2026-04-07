# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        carry = 0
        current = dummy

        while l1 or l2 or carry:
            if l1:
                sum1 = l1.val
                l1 = l1.next
            else:
                sum1 = 0
            if l2:
                sum2 = l2.val
                l2 = l2.next
            else:
                sum2 = 0
            
            total = sum1 + sum2 + carry 
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next
        
        return dummy.next


