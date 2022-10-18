from pytest import fixture

from PROBLEM_NAME import Solution


@fixture
def s() -> Solution:
    return Solution()
