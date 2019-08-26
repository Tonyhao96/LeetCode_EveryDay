#21_Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ls1, ls2=l1, l2
        ls=ListNode(None)
        head=ListNode(None)
        head.next=ls
        
        while ls1 and ls2:
            if ls1.val<ls2.val:
                ls.next=ls1
                ls1=ls1.next
                ls=ls.next
            else:
                ls.next=ls2
                ls2=ls2.next
                ls=ls.next
        ls.next=ls1 or ls2
        return head.next.next
