# 2_Add Two Numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# To int and list Recursion
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def toint(ls):
            return ls.val+10*toint(ls.next) if ls else 0

        def tols(it):
            ls = ListNode(it % 10)
            if it > 9:
                ls.next = tols(it//10)
            return ls
        return tols(toint(l1)+toint(l2))


# Iteration
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = temp = ListNode(0)
        sum_ls = 0
        while l1 or l2 or sum_ls:
            if l1:
                sum_ls += l1.val
                l1 = l1.next
            if l2:
                sum_ls += l2.val
                l2 = l2.next
            temp.next = ListNode(sum_ls % 10)
            temp = temp.next
            sum_ls //= 10
        return result.next
