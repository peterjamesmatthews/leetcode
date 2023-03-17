from problem_name import Solution  # TODO replace PROBLEM_NAME
from pytest import fixture


@fixture
def s() -> Solution:
    return Solution()


def test_example(s: Solution):
    """
    Write tests like this
    """
    assert s != None
