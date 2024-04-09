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


def test_XLV(s: Solution):
    assert s.romanToInt("XLV") == 45


def test_CDXLV(s: Solution):
    assert s.romanToInt("CDXLV") == 445


def test_CXLV(s: Solution):
    assert s.romanToInt("CXLV") == 145


def test_X(s: Solution):
    assert s.romanToInt("X") == 10


def test_D(s: Solution):
    assert s.romanToInt("D") == 500
