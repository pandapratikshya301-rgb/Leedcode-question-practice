class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()

        new = ""

        for char in s:
            if char.isalnum():
                new += char

        return new == new[::-1]