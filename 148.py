# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        item = head
        l = []
        while(item is not None):
            l.append(item.val)
            item = item.next
        l.sort()
        item = head
        for i in range(len(l)):
            item.val = l[i]
            item = item.next
        return head