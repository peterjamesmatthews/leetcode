from pytest import fixture

from rotate_list import Solution, ListNode


@fixture
def s() -> Solution:
    return Solution()


def test_list_node_repr():
    l = ListNode(1, ListNode(2))
    assert l.__repr__() == "<1 -> 2>"
    assert l.next.__repr__() == "<2 -> None>"


def test_shift_by_0(s: Solution):
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    l = s.rotateRight(l, 0)
    assert str(l) == "[1, 2, 3, 4, 5]"


def test_shift_by_1(s: Solution):
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    l = s.rotateRight(l, 1)
    assert str(l) == "[5, 1, 2, 3, 4]"


def test_shift_by_2(s: Solution):
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    l = s.rotateRight(l, 2)
    assert str(l) == "[4, 5, 1, 2, 3]"


def test_shift_by_5(s: Solution):
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    l = s.rotateRight(l, 5)
    assert str(l) == "[1, 2, 3, 4, 5]"


def test_shift_by_6(s: Solution):
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    l = s.rotateRight(l, 6)
    assert str(l) == "[5, 1, 2, 3, 4]"


def test_shift_by_7(s: Solution):
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    l = s.rotateRight(l, 7)
    assert str(l) == "[4, 5, 1, 2, 3]"


def test_shift_by_negative_1(s: Solution):
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    l = s.rotateRight(l, -1)
    assert str(l) == "[2, 3, 4, 5, 1]"


def test_shift_by_negative_2(s: Solution):
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    l = s.rotateRight(l, -2)
    assert str(l) == "[3, 4, 5, 1, 2]"


def test_shift_by_negative_5(s: Solution):
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    l = s.rotateRight(l, -5)
    assert str(l) == "[1, 2, 3, 4, 5]"


def test_shift_by_negative_6(s: Solution):
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    l = s.rotateRight(l, -6)
    assert str(l) == "[2, 3, 4, 5, 1]"
