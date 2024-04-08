from typing import List
import pytest
from two_out_of_three import Solution


@pytest.fixture
def s() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "nums1,nums2,nums3,want",
    [
        pytest.param([], [], [], [], id="empty"),
        pytest.param([1, 1, 3, 2], [2, 3], [3], [3, 2], id="example one"),
        pytest.param([3, 1], [2, 3], [1, 2], [2, 3, 1], id="example two"),
        pytest.param([1, 2, 2], [4, 3, 3], [5], [], id="example three"),
    ],
)
def test_Solution(
    s: Solution,
    nums1: List[int],
    nums2: List[int],
    nums3: List[int],
    want: List[int],
):
    got = s.twoOutOfThree(nums1, nums2, nums3)
    assert set(got) == set(want), f"got != want ({got} != {want})"
