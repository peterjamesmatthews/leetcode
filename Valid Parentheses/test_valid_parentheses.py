from pytest import fixture

from valid_parentheses import Solution


@fixture
def s() -> Solution:
    return Solution()


def test_one_opener(s: Solution):
    assert s.isValid("[") == False
    assert s.isValid("(") == False
    assert s.isValid("{") == False


def test_three_sequential_pairs(s: Solution):
    assert s.isValid("()[]{}") == True


def test_unmatched_outer_pair(s: Solution):
    assert s.isValid("([][][][]]") == False


def test_long_invalid(s: Solution):
    assert s.isValid("[" * 5 + "]" * 6) == False


def test_long_valid(s: Solution):
    assert s.isValid("[" * 10 + "]" * 10) == True


def test_many_valid_pairs(s: Solution):
    assert s.isValid("[]{}()" * 100) == True


def test_open_with_closer(s: Solution):
    assert s.isValid("}[") == False
