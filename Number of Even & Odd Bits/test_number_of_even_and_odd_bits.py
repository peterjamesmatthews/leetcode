from number_of_even_and_odd_bits import Solution
import pytest


@pytest.fixture
def s() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "n,want",
    [
        pytest.param(0, [0, 0], id="empty"),
        pytest.param(17, [2, 0], id="seventeen"),
        pytest.param(2, [0, 1], id="two"),
    ],
)
def test_solution(s: Solution, n, want):
    got = s.evenOddBit(n)
    assert got == want, f"got != want, {got} != {want}"
