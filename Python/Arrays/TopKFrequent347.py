class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            freq[c].append(n)

        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        min_heap = []
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num)) #auto sorted by first element of tuple

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for freq, num in min_heap]
        