from pytest import fixture

from PROBLEM_NAME import Solution  # TODO replace PROBLEM_NAME


@fixture
def s() -> Solution:
    return Solution()


def test_example(s: Solution):
    """
    Write tests like this
    """
    assert s != None
