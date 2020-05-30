
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        import heapq
        count = collections.Counter(nums)
        heap = [(-freq, number) for (number, freq) in count.items()]
        heapq.heapify(heap)
        res = [heapq.heappop(heap)[1] for _ in range(k)]
        return res


nums = [1,1,1,2,2,3]
k = 2
s1 = Solution()
print(s1.topKFrequent(nums, k))