#面试题06.从尾到头打印链表

#Using List
#Time complexity: O(n)  Space complexity: O(n)
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res.reverse() #res[::-1]
        return res

#Using Recursive Method
#Time complexity: O(n)  Space complexity: O(n)
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head: return []
        return self.reversePrint(head.next) + [head.val]

#Using Stack
#Time complexity: O(n)  Space complexity: O(n)
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack, res = [], []
        while head:
            stack.append(head.val)
            head = head.next
        while stack:
            res.append(stack.pop())
        return res
        