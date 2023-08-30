from typing import List


class Solution:
    """
    @name: 238. Product of Array Except Self
    @url: https://leetcode.com/problems/product-of-array-except-self/
    @deps: Array, Prefix Sum
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        postfix = 1

        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


if __name__ == "__main__":
    nums = [-1, 1, 0, -3, 3]
    s = Solution()
    print(s.productExceptSelf(nums))
