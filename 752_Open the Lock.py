# 752_Open the Lock

# Using BFS
from queue import Queue


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends:
            return -1

        q = Queue()
        q.put(('0000', 0))  # Step = 0
        while not q.empty():
            node, step = q.get()
            for i in range(4):
                for one in (1, -1):
                    current = node[:i] + \
                        str((int(node[i])+one) % 10) + node[i+1:]
                    if current == target:
                        return step+1
                    if not current in deadends:
                        q.put((current, step+1))
                        deadends.add(current)
        return -1
