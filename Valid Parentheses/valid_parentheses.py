"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:

    _CLOSERS_ = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    def isValid(self, s: str) -> bool:
        if not s or len(s) % 2 == 1:
            return False
        openers = []
        # iterate over s
        for char in s:
            if char in ["(", "[", "{"]:  # char is an opener
                # add opener to a stack
                openers.append(char)
            else:
                if len(openers) == 0 or Solution._CLOSERS_[char] != openers[-1]:
                    return False
                openers.pop()
        return True
