from pytest import fixture

from contains_duplicate import Solution


@fixture
def s() -> Solution:
    return Solution()


def test_example_one(s: Solution):
    assert s.containsDuplicate([1, 2, 3, 1])


def test_example_two(s: Solution):
    assert not s.containsDuplicate([1, 2, 3, 4])


def test_example_three(s: Solution):
    assert s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
