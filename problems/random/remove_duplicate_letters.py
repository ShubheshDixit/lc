class Solution:
    '''
    @name: Remove Duplicate letters
    @url: https://leetcode.com/problems/remove-duplicate-letters/
    @deps: string, stack, greedy, monotnoic stack
    @question:
        Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
        Example 1:

        Input: s = "bcabc"
        Output: "abc"
        Example 2:

        Input: s = "cbacdcbc"
        Output: "acdb"


        Constraints:

        1 <= s.length <= 104
        s consists of lowercase English letters.


        Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

    '''

    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        visited = set()
        last_index = {c: i for i, c in enumerate(s)}

        for i in range(len(s)):
            if s[i] in visited:
                continue
            else:
                while len(stack) > 0 and s[i] < stack[-1] and last_index[stack[-1]] > i:
                    visited.remove(stack.pop())
                stack.append(s[i])
                visited.add(s[i])
        return ("").join(stack)


if __name__ == "__main__":
    s = "cbacdcbc"
    res = Solution().removeDuplicateLetters(s)
    print(res)


'''

cbacdcbc
01234567
dic = {
    c: 3,
    b: 6,
    d: 4,
    a: 2,
} 

stack = [
    c
    b

]

last_i = {
    c: 7,
    b: 6,
    d: 4,
    a: 2
}

visi = {
    c: False,
    b: False,
    d: False,
    a: False
}

stack = [
]

'''
