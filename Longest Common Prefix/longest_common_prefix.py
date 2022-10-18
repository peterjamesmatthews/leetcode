"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""  # running prefix
        while True:
            try:
                char = strs[0][len(prefix)]  # get potential char from first string
                for string in strs[1:]:  # compare chars from subsequent strings
                    assert string[len(prefix)] == char
                prefix += char  # each string contains char, add it to prefix
            except:  # most likely index of out bounds or assertion
                return prefix
