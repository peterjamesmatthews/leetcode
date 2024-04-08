from typing import List
from number_of_students_unable_to_eat_lunch import Solution
import pytest


@pytest.fixture
def s() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "students,sandwiches,want",
    [
        pytest.param([], [], 0, id="empty"),
        pytest.param([1, 1, 0, 0], [0, 1, 0, 1], 0, id="4 students with 0 unable"),
        pytest.param(
            [1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1], 3, id="6 student with 3 unable"
        ),
    ],
)
def test_count_students(
    s: Solution, students: List[int], sandwiches: List[int], want: int
):
    got = s.countStudents(students, sandwiches)
    assert got == want, f"Expected {want}, but got {got}"
