# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val =[]
        curr =head
        while curr:
            val.append(curr.val)
            curr = curr.next
        val.sort()
        temp = ListNode(0)
        curr = temp
        for i in range (len(val)):
            curr.next = ListNode(val[i])
            curr = curr.next
        return temp.next