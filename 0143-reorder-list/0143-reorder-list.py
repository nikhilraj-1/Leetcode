# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2= slow.next
        slow.next=None
        head3=self.reverseList(head2)
        first,second = head,head3
        while second:
            t1,t2=first.next,second.next
            first.next=second
            second.next=t1
            first,second=t1,t2

    def reverseList(self,head:Optional[ListNode])->Optional[ListNode]:
        prev = None
        curr =head
        while curr:
            next = curr.next
            curr.next=prev
            prev = curr
            curr=next
        return prev



        
        