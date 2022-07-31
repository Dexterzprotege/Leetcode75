# Question: https://leetcode.com/problems/last-stone-weight/

# Solution: Heaps:
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            w1 = heapq.heappop(heap)
            w2 = heapq.heappop(heap)
            if w1 == w2:
                continue
            else:
                heapq.heappush(heap, w1-w2)
        
        return -heapq.heappop(heap) if len(heap) == 1 else 0
      
# Verdict
# Runtime: 29 ms, faster than 97.37% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 13.8 MB, less than 62.46% of Python3 online submissions for Last Stone Weight.

# ----------------------------------------------------------------------------------------------------
  
# Solution:
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            w1 = max(stones)
            stones.remove(w1)
            w2 = max(stones)
            stones.remove(w2)
            if w1 == w2:
                continue
            else:
                stones.append(abs(w2-w1))
        return stones[0] if len(stones) == 1 else 0
      
# Verdict:
# Runtime: 60 ms, faster than 22.73% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 13.7 MB, less than 97.30% of Python3 online submissions for Last Stone Weight.
