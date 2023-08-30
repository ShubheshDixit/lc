from typing import List


class Solution:
    """
    @name: 659. Encode and Decode Strings
    @url: https://leetcode.com/problems/encode-and-decode-strings/
    @deps: String
    """

    def encode(self, strs: List[str]) -> str:
        # write your code here
        return "".join([str(len(s)) + ":" + s for s in strs])

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, string: str) -> List[str]:
        # write your code here
        res = []
        i = 0
        while i < len(string):
            j = string.find(":", i)
            i = j + 1 + int(string[i:j])
            res.append(string[j + 1 : i])

        return res


if __name__ == "__main__":
    strs = ["we", "say", ":", "yes"]
    s = Solution()
    print(s.encode(strs))
    print(s.decode(s.encode(strs)))
