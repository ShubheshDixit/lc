
class Solution:
    '''
    @name: Strong Password Checker
    @url: https://leetcode.com/problems/strong-password-checker/
    @deps: string, greedy, heap(priority queue)
    @question:
        A password is considered strong if the below conditions are all met:

        It has at least 6 characters and at most 20 characters.
        It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
        It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
        Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

        In one step, you can:

        Insert one character to password,
        Delete one character from password, or
        Replace one character of password with another character.


        Example 1:

        Input: password = "a"
        Output: 5
        Example 2:

        Input: password = "aA1"
        Output: 3
        Example 3:

        Input: password = "1337C0d3"
        Output: 0


        Constraints:

        1 <= password.length <= 50
        password consists of letters, digits, dot '.' or exclamation mark '!'.
    '''

    def strongPasswordChecker(self, password: str) -> int:
        lwr = 1
        upr = 1
        dg = 1
        repeating = 0

        for i, c in enumerate(password):
            if c.isdigit():
                dg = 0
            if c.islower():
                lwr = 0
            if c.isupper():
                upr = 0
        missing = (dg + lwr + upr)
        i = 0
        while (i < len(password) - 2):
            if password[i] == password[i+1] and password[i+1] == password[i+2]:
                repeating += 1
                i += 3
            else:
                i += 1
        print(missing, repeating, len(password))
        if len(password) < 6:
            return max(missing, 6 - len(password))
        if len(password) <= 20:
            return max(missing, min(repeating, missing + repeating) if repeating >= missing else max(repeating, (missing + repeating)))

        else:
            return max(len(password) - 20 + max(repeating - repeating // 3, missing), repeating)


if __name__ == "__main__":
    # password = "a"
    # password = "1337C0d3"
    # password = "aA1"
    # password = "aaa111"
    # password = "1111111111"
    # password = "bbaaaaaaaaaaaaaaacccccc"
    password = "axaaAAAAAA000000123456"
    res = Solution().strongPasswordChecker(password)
    print(res)


'''
bbaaaaaaaaaaaaaaacccccc

d = 1
u = 1


5 // 3 = 2

5 % 3 = 2



'''
