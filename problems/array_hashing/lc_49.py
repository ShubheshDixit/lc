from collections import defaultdict
from typing import List


class Solution:
    """
    @name: 49. Group Anagrams
    @url: https://leetcode.com/problems/group-anagrams/
    @deps: Array, Hash Table, String, Sorting
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[str(count)].append(s)

        return res.values()


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = Solution().groupAnagrams(strs)
    print(res)
