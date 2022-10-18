from pytest import fixture

from roman_to_integer import Solution


@fixture
def s() -> Solution:
    return Solution()


def test_empty_string(s: Solution):
    assert s.romanToInt("") == 0


def test_I(s: Solution):
    assert s.romanToInt("I") == 1


def test_III(s: Solution):
    assert s.romanToInt("III") == 3


def test_LVIII(s: Solution):
    assert s.romanToInt("LVIII") == 58


def test_MCMXCIV(s: Solution):
    assert s.romanToInt("MCMXCIV") == 1994


def test_MMMCMXCIX(s: Solution):
    assert s.romanToInt("MMMCMXCIX") == 3999
