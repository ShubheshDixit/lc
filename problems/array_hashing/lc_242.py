class Solution:
    """
    @name: 242. Valid Anagram
    @url: https://leetcode.com/problems/valid-anagram/
    @deps: Hash Table, Sort, String
    """

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}
        for i in range(len(s)):
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            t_count[t[i]] = 1 + t_count.get(t[i], 0)
        return s_count == t_count


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    res = Solution().isAnagram(s, t)
    print(res)
