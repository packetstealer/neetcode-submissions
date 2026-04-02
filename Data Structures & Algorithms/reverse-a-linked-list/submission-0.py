# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        [0] -> [1] -> [2] -> [3]
        pointer to keep track of new head as you traverse list
        pointer to keep track of previous head
        set new head to be next node
        set head.next of new head to the previous head
        """
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev