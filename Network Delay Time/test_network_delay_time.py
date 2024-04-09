from typing import List
from network_delay_time import Solution
import pytest


@pytest.fixture
def s() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "times,n,k,want",
    [
        pytest.param([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2, id="example one"),
        pytest.param([[1, 2, 1]], 2, 1, 1, id="example two"),
        pytest.param([[1, 2, 1]], 2, 2, -1, id="example three"),
        pytest.param([[1, 2, 1], [2, 1, 1]], 2, 1, 1, id="basic cycle"),
    ],
)
def test_solution(s: Solution, times: List[List[int]], n: int, k: int, want: int):
    got = s.networkDelayTime(times, n, k)
    assert got == want, f"got != want, {got} != {want}"
