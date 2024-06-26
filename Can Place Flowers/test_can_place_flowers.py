from can_place_flowers import Solution
from pytest import fixture


@fixture
def s() -> Solution:
    return Solution()


def test_10001_1(s: Solution):
    assert s.canPlaceFlowers([1, 0, 0, 0, 1], 1)


def test_10001_2(s: Solution):
    assert not s.canPlaceFlowers([1, 0, 0, 0, 1], 2)


def test_0_1(s: Solution):
    assert s.canPlaceFlowers([0], 1)


def test_000_2(s: Solution):
    assert s.canPlaceFlowers([0, 0, 0], 2)


def test_100_1(s: Solution):
    assert s.canPlaceFlowers([1, 0, 0], 1)


def test_001_1(s: Solution):
    assert s.canPlaceFlowers([0, 0, 1], 1)


def test_100001_2(s: Solution):
    assert not s.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2)
