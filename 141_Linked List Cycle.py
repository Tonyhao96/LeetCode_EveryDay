#141_Linked List Cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Using Hash
#Time complexity: O(n)  Space complexity: O(n)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        cache = set()
        while head:
            if head in cache:
                return True
            cache.add(head)
            head = head.next
        return False

#Using Fast and Slow Pointer
#Time complexity: O(n+k)  Space complexity: O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
