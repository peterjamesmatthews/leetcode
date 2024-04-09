from typing import List
from time_needed_to_buy_tickets import Solution
import pytest


@pytest.fixture
def s() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "tickets,k,want",
    [
        pytest.param([2, 3, 2], 2, 6, id="first example"),
        pytest.param([5, 1, 1, 1], 0, 8, id="second example"),
    ],
)
def test_solution(s: Solution, tickets: List[int], k: int, want: int):
    got = s.timeRequiredToBuy(tickets, k)
    assert got == want, f"got != want, {got} != {want}"
