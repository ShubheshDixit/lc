class Solution:
    """
    @name: 125. Valid Palindrome
    @url: https://leetcode.com/problems/valid-palindrome/
    @deps: Two Pointers, String
    """

    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1

            while i < j and not s[j].isalnum():
                j -= 1

            if i < j and s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True


if __name__ == "__main__":
    s = Solution()
    st = "A man, a plan, a canal: Panama"
    print(s.isPalindrome(st))
