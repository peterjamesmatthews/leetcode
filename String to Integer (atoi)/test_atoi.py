from atoi import Solution
import pytest


@pytest.fixture
def s() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "a,want",
    [
        pytest.param("", 0, id="empty"),
        pytest.param("0", 0, id="zero"),
        pytest.param("42", 42, id="forty-two"),
        pytest.param("+42", 42, id="positive forty-two"),
        pytest.param("   -42", -42, id="negative forty-two with leading whitespace"),
        pytest.param(
            "4193 with words", 4193, id="four thousand ninety three with trailing words"
        ),
    ],
)
def test_solution(s: Solution, a: str, want):
    got = s.myAtoi(a)
    assert got == want, f"got != want, {got} != {want}"
