#234_Palindrome Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        val=[]
        while head:
            val += head.val,
            head=head.next
        return val==val[::-1]