from pytest import fixture
from valid_anagram import Solution


@fixture
def s() -> Solution:
    return Solution()


def test_example_one(s: Solution):
    assert s.isAnagram("anagram", "nagaram")


def test_example_two(s: Solution):
    assert not s.isAnagram("rat", "car")


def test_aa_bb(s: Solution):
    assert not s.isAnagram("aa", "bb")


def test_abc_abcd(s: Solution):
    assert not s.isAnagram("abc", "abcd")
