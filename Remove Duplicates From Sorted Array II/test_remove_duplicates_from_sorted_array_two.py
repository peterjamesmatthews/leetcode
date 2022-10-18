from pytest import fixture

from remove_duplicates_from_sorted_array_two import Solution


@fixture
def s() -> Solution:
    return Solution()


def test_one_one_two(s: Solution):
    nums = [1, 1, 2]
    assert s.removeDuplicates(nums) == 3
    assert nums[:3] == [1, 1, 2]


def test_longer(s: Solution):
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert s.removeDuplicates(nums) == 9
    assert nums[:9] == [0, 0, 1, 1, 2, 2, 3, 3, 4]


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
    assert s.removeDuplicates(nums) == 6
    assert nums[:6] == [1, 1, 2, 2, 3, 3]


def test_most_dupes(s: Solution):
    nums = []
    for i in range(int(3e4 / 2)):
        nums.append(i)
        nums.append(i)
    assert s.removeDuplicates(nums) == 3e4
    i = 0
    while i < 3e4 - 2:
        assert nums[i] == nums[i + 1]
        i += 2
