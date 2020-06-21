#面试题09.用两个栈实现队列

class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None: #Time complexity: O(1)  Space complexity: O(1)
        self.stack1.append(value)

    def deleteHead(self) -> int:  #Time complexity: O(n)  Space complexity: O(n)
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else -1
