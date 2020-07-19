#面试题 02.05. 链表求和

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Calculate Sum first
#Time complexity: O(3n)  Space complexity: O(n)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def sumlist(x):
            s = i = 0
            while x:
                s += x.val * 10 ** i
                i += 1
                x = x.next
            return s
        sl = sumlist(l1) + sumlist(l2)
        a = ListNode(0)
        res = a
        while sl:
            a.next = ListNode(sl % 10)
            sl = sl // 10
            a = a.next
        return res.next
