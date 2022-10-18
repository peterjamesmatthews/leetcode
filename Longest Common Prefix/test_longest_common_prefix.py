from pytest import fixture

from longest_common_prefix import Solution


@fixture
def s() -> Solution:
    return Solution()


def test_three_asdf(s: Solution):
    assert s.longestCommonPrefix(["asdf"] * 3) == "asdf"


def test_no_prefix(s: Solution):
    assert s.longestCommonPrefix(["asdf", "wer", "xzcv"]) == ""


def test_three_empty_strings(s: Solution):
    assert s.longestCommonPrefix([""] * 3) == ""


def test_one_empty_strs(s: Solution):
    assert s.longestCommonPrefix([""]) == ""


def test_three_similar_strs(s: Solution):
    assert s.longestCommonPrefix(["asdf", "asdvv", "asdsg"]) == "asd"
