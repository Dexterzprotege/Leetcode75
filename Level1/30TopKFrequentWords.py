# Question: https://leetcode.com/problems/top-k-frequent-words/

# Solution: Heaps:
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = defaultdict(int)
        for word in words:
            dic[word] += 1
        
        heap = [(-val, key) for key, val in dic.items()]
        heapq.heapify(heap)
        ans = []
        
        for i in range(k):
            item = heapq.heappop(heap)
            ans.append(item[-1])
        
        return ans
      
# Verdict:
# Runtime: 56 ms, faster than 96.38% of Python3 online submissions for Top K Frequent Words.
# Memory Usage: 13.9 MB, less than 64.69% of Python3 online submissions for Top K Frequent Words.

# --------------------------------------------------------------------------------------------------

# Solution:
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = defaultdict(int)
        for word in words:
            dic[word] += 1
        
        res = sorted(dic, key=lambda x: (-dic[x], x))
        return res[:k]
      
# Verdict:
# Runtime: 105 ms, faster than 27.88% of Python3 online submissions for Top K Frequent Words.
# Memory Usage: 14 MB, less than 27.03% of Python3 online submissions for Top K Frequent Words.
