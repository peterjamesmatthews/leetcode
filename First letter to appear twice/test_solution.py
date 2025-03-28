from solution import Solution
import pytest


@pytest.fixture
def s() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "input,want",
    [
        pytest.param("asdfjkl;a", "a", id="empty str"),
        pytest.param("abcdd", "d", id="abcdd"),
    ],
)
def test_solution(s: Solution, input: str, want: str):
    got = s.repeatedCharacter(input)
    assert got == want, f"got != want, {got} != {want}"
