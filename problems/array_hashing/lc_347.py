from typing import List


class Solution:
    """
    @name: 347. Top K Frequent Elements
    @url: https://leetcode.com/problems/top-k-frequent-elements/
    @deps: Hash Table, Heap
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        arr = [[] for _ in range(len(nums) + 1)]
        top_k_frequent = []

        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1

        for key, value in frequency_map.items():
            arr[value].append(key)

        for i in range(len(arr) - 1, 0, -1):
            for n in arr[i]:
                top_k_frequent.append(n)
                if len(top_k_frequent) == k:
                    return top_k_frequent


"""
      [3]  [2] [2, 4]
    0 1 2 3 4 

"""

if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    s = Solution()
    print(s.topKFrequent(nums, k))
