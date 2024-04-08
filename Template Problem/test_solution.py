from solution import Solution
import pytest


@pytest.fixture
def s() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "want",
    [
        # pytest.param(*args, want, id="<test case id>")
    ],
)
def test_solution(s: Solution, want):
    # got = s.<method>(...)
    # assert got == want, f"got != want, {got} != {want}"
    ...
