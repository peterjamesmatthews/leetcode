"""
Given a string `s`, find the length of the longest substring without repeating characters.
"""
from typing import Set


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Tracks a dynamically sized sliding substring along the entirety of `s`.

        If a character is about to end the substring that's already a member...
        1. Compare the current substring's length to a running maximum.
        2. Slide the start of the substring forward, past the original (now repeated) character.

        #### `Time-complexity: O(len(s))`
        the entirety of `s` as to be considered

        #### `Space-complexity: O(len(s))`
        we need to track a `Set` of the substring's characters, and the substring could be equal to `s`


        #### Examples
        ```py
        lengthOfLongestSubstring("abcabcbb") == 3  # "abcabcbb"'s longest substring is "abc" which has a length of 3
        ```
        ```py
        lengthOfLongestSubstring("bbbbb") == 1  # "bbbbb"'s longest substring is "b" which has a length of 1
        ```
        ```py
        lengthOfLongestSubstring("pwwkew") == 3  # "pwwkew"'s longest substring is either "wke" or "kew" which both have a length of 3
        ```

        Args:
            `s: str` -  string to search from

        Returns:
            `int` - length of the longest substring of distinct characters in `s`
        """
        max_len = 0  # running maximum length of substring
        start = 0  # starting index of substring
        end = 0  # ending index of substring
        chars: Set[str] = set()  # set to hold members of substring
        while end < len(s):  # O(len(s))
            if s[end] in chars:  # repeated character is about to enter substring
                max_len = max(
                    len(chars), max_len
                )  # compare current substring's length to running maximum
                while (
                    s[start] != s[end]
                ):  # advance the substring's start until repeated character is found
                    chars.remove(
                        s[start]
                    )  # characters exiting the substring don't need to be tracked
                    start += 1  # advance the substring's start
                else:  # s[start] == s[end]
                    start += 1  # advance the substring's start
            chars.add(s[end])
            end += 1  # grow the substring
        else:
            max_len = max(
                len(chars), max_len
            )  # compare final substring's length to running maximum
        return max_len
