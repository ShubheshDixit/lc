from typing import List


class Solution:
    """
    @questions: 15. 3Sum
    @url: https://leetcode.com/problems/3sum/
    @deps: Array, Two Pointers, Sorting
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = num + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([num, nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1

                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(s.threeSum(nums))
