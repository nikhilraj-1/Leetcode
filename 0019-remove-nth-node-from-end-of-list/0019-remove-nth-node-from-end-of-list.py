# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next == None and n==1 :
            return None

        count =0
        curr = head
        while curr:
            count+=1
            curr=curr.next
        
        pos = count -n + 1
        curr = head
        if pos == 1:
            return curr.next
        while pos>2 :
            curr = curr.next
            pos-=1
        free = curr.next
        curr.next = free.next

        return head
