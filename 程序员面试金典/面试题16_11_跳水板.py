#面试题 16.11. 跳水板

#Using Arithmetic Progression
#Time complexity: O(k)  Space complexity: O(1)

class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if not k:
            return []
        if shorter == longer:
            return [k*shorter]
        else:
            return list(range(k*shorter, k*longer+1, longer-shorter))
