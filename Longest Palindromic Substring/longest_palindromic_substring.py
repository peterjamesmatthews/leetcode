"""
Given a string `s`, return _the longest palindromic substring_ in `s`.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = [0, 1]
        palindrome = [0, 1]
        center = [0, 1]

        while center[0] < len(s) - 1:
            # find next center
            match center[1] - center[0]:
                case 1:
                    if center[1] < len(s) and s[center[0]] == s[center[1]]:
                        center[1] += 1
                        if longest[1] - longest[0] < 2:
                            longest[0], longest[1] = center[0], center[1]
                    else:
                        center[0] += 1
                        center[1] += 1
                case 2:
                    center[0] += 1

            palindrome[0], palindrome[1] = center

            while palindrome[0] > 0 and palindrome[1] < len(s):
                # check boundary
                if s[palindrome[0] - 1] == s[palindrome[1]]:
                    # grow
                    palindrome[0] -= 1
                    palindrome[1] += 1
                    if palindrome[1] - palindrome[0] > longest[1] - longest[0]:
                        longest = [palindrome[0], palindrome[1]]
                else:
                    break

        return s[longest[0] : longest[1]]
