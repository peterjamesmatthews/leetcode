from pytest import fixture

from binary_tree_pruning import Solution


@fixture
def s() -> Solution:
    return Solution()


def test_first_example(s: Solution):
    """
    Only the red nodes satisfy the property "every subtree not containing a 1". The
    diagram on the right represents the answer.

    https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png
    """
    assert s.pruneTree([1, None, 0, 0, 1]) == [1, None, 0, None, 1]


def test_second_example(s: Solution):
    assert s.pruneTree([1, 0, 1, 0, 0, 0, 1]) == [1, None, 1, None, 1]


def test_third_example(s: Solution):
    assert s.pruneTree([1, 1, 0, 1, 1, 0, 1, 0]) == [1, 1, 0, 1, 1, None, 1]
