from pytest import fixture

from remove_duplicates_from_sorted_array import Solution


@fixture
def s() -> Solution:
    return Solution()


def test_one_one_two(s: Solution):
    nums = [1, 1, 2]
    assert s.removeDuplicates(nums) == 2
    assert nums[:2] == [1, 2]


def test_longer(s: Solution):
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert s.removeDuplicates(nums) == 5
    assert nums[:5] == [0, 1, 2, 3, 4]


def test_one(s: Solution):
    nums = [1]
    assert s.removeDuplicates(nums) == 1
    assert nums[:1] == [1]


def test_none(s: Solution):
    nums = []
    assert s.removeDuplicates([]) == 0
    assert nums == []


def test_longest(s: Solution):
    nums = list(range(0, int(3e4)))
    assert s.removeDuplicates(nums) == int(3e4)
    assert nums == list(range(0, int(3e4)))


def test_longest_with_dupes(s: Solution):
    nums = [1] * int(1e4) + [2] * int(1e4) + [3] * int(1e4)
    assert s.removeDuplicates(nums) == 3
    assert nums[:3] == [1, 2, 3]
