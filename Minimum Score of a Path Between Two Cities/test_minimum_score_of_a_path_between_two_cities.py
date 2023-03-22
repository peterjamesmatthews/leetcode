from minimum_score_of_a_path_between_two_cities import Solution
from pytest import fixture


@fixture
def s() -> Solution:
    return Solution()


def test_example_one(s: Solution):
    assert s.minScore(4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]) == 5


def test_example_two(s: Solution):
    assert s.minScore(4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]]) == 2


def test_smallest(s: Solution):
    assert s.minScore(2, [[1, 2, 4]]) == 4
    assert s.minScore(2, [[2, 1, 4]]) == 4
