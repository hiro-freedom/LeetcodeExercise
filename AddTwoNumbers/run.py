# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        pl1 = l1
        pl2 = l2
        carry = 0
        p_node = None

        while pl1 != None or pl2 != None or carry != 0:
            a = pl1.val if pl1 != None else 0
            b = pl2.val if pl2 != None else 0

            x = a+b+ carry

            carry = x//10
            x = x % 10

            if result == None:
                result = ListNode(x)
                p_node = result
            else :
                p_node.next = ListNode(x)
                p_node = p_node.next

            pl1 = pl1.next if pl1 != None else None
            pl2 = pl2.next if pl2 != None else None

        return result


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

a = Solution()
res = a.addTwoNumbers(l1, l2)
print(res.val)
print(res.next.val)
print(res.next.next.val)
