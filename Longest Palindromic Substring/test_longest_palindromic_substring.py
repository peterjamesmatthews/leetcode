from longest_palindromic_substring import Solution
from pytest import fixture


@fixture
def s() -> Solution:
    return Solution()


def test_babad(s: Solution):
    assert s.longestPalindrome("babad") == "bab"


def test_cbbd(s: Solution):
    assert s.longestPalindrome("cbbd") == "bb"


def test_a(s: Solution):
    assert s.longestPalindrome("a") == "a"


def test_ccc(s: Solution):
    assert s.longestPalindrome("ccc") == "ccc"


def test_cc(s: Solution):
    assert s.longestPalindrome("cc") == "cc"
