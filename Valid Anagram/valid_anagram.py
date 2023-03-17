"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [[0, 0] for _ in range(26)]

        for i in range(len(s)):
            counts[ord(s[i]) % 26][0] += 1
            counts[ord(t[i]) % 26][1] += 1

        return all(map(lambda count: count[0] == count[1], counts))
