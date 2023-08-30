from typing import List, Set


class Solution:
    """
    @name: 217. Contains Duplicate
    @url: https://leetcode.com/problems/contains-duplicate/
    @deps: Array, Hash Table, Sorting
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        values: Set[int] = set()

        for num in nums:
            if num in values:
                return True
            values.add(num)

        return False


if __name__ == "__main__":
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    res = Solution().containsDuplicate(nums)
    print(res)
