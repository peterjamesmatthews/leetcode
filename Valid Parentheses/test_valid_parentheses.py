from pytest import fixture

from valid_parentheses import Solution


@fixture
def s() -> Solution:
    return Solution()


def test_one_opener(s: Solution):
    assert s.isValid("[") is False
    assert s.isValid("(") is False
    assert s.isValid("{") is False


def test_three_sequential_pairs(s: Solution):
    assert s.isValid("()[]{}") is True


def test_unmatched_outer_pair(s: Solution):
    assert s.isValid("([][][][]]") is False


def test_long_invalid(s: Solution):
    assert s.isValid("[" * 5 + "]" * 6) is False


def test_long_valid(s: Solution):
    assert s.isValid("[" * 10 + "]" * 10) is True


def test_many_valid_pairs(s: Solution):
    assert s.isValid("[]{}()" * 100) is True


def test_mismatch_closer_opener(s: Solution):
    assert s.isValid("}[") is False


def test_matched_closer_opener(s: Solution):
    assert s.isValid("][") is False


def test_closers(s: Solution):
    assert s.isValid("}]") is False
