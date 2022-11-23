from pytest import fixture

from longest_substring_without_repeating_characters import (
    Solution,
)


@fixture
def s() -> Solution:
    return Solution()


def test_example_one(s: Solution):
    assert (
        s.lengthOfLongestSubstring("abcabcbb") == 3
    ), """
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
		"""


def test_example_two(s: Solution):
    assert (
        s.lengthOfLongestSubstring("bbbbb") == 1
    ), """
	Input: s = "bbbbb"
	Output: 1
	Explanation: The answer is "b", with the length of 1.
	"""


def test_example_three(s: Solution):
    assert (
        s.lengthOfLongestSubstring("pwwkew") == 3
    ), """
	Input: s = "pwwkew"
	Output: 3
	Explanation: The answer is "wke", with the length of 3.
	Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
	"""
