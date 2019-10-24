# 1046_Last Stone Weight

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            diff = stones[-1]-stones[-2]
            del stones[-2:]
            if diff:
                stones.append(diff)
        return stones[0] if stones else 0

# Using Heapq
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)
        
        while len(stones)>1:
            largest = heapq.nlargest(2, stones)
            diff = abs(largest[0]-largest[1])
            
            for item in largest:
                stones.remove(item)
            
            if diff > 0:
                heapq.heappush(stones, diff)
                
        if stones:
            return stones[0]
        return 0