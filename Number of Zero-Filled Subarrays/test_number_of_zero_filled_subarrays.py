from number_of_zero_filled_subarrays import Solution
from pytest import fixture


@fixture
def s() -> Solution:
    return Solution()


def test_1(s: Solution):
    assert s.zeroFilledSubarray([1]) == 0


def test_0(s: Solution):
    assert s.zeroFilledSubarray([0]) == 1


def test_13002004(s: Solution):
    assert s.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]) == 6


def test_000200(s: Solution):
    assert s.zeroFilledSubarray([0, 0, 0, 2, 0, 0]) == 9


def test_2102019(s: Solution):
    assert s.zeroFilledSubarray([2, 10, 2019]) == 0
