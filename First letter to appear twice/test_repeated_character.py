from typing import Optional
from repeated_character import Solution
import pytest


@pytest.fixture
def s() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "input,want,err",
    [
        pytest.param("asdfjkl;a", "a", None, id="empty str"),
        pytest.param("abcdd", "d", None, id="abcdd"),
        pytest.param("", "d", ValueError("s must contain one repeat letter"), id="empty str"),
    ],
)
def test_solution(s: Solution, input: str, want: Optional[Exception], err: Optional[Exception]):
    try:
        got = s.repeatedCharacter(input)
        assert got == want, f"got != want, {got} != {want}"
    except Exception as e:
        assert str(e) == str(err), f"e != err, {e} != {err}"
