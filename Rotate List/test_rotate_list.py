from pytest import fixture
from rotate_list import ListNode, Solution


@fixture
def s() -> Solution:
    return Solution()


def test_list_node_repr():
    nodes = ListNode(1, ListNode(2))
    assert nodes.__repr__() == "<1 -> 2>"
    assert nodes.next.__repr__() == "<2 -> None>"


def test_shift_by_0(s: Solution):
    nodes = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    nodes = s.rotateRight(nodes, 0)
    assert str(nodes) == "[1, 2, 3, 4, 5]"


def test_shift_by_1(s: Solution):
    nodes = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    nodes = s.rotateRight(nodes, 1)
    assert str(nodes) == "[5, 1, 2, 3, 4]"


def test_shift_by_2(s: Solution):
    nodes = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    nodes = s.rotateRight(nodes, 2)
    assert str(nodes) == "[4, 5, 1, 2, 3]"


def test_shift_by_5(s: Solution):
    nodes = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    nodes = s.rotateRight(nodes, 5)
    assert str(nodes) == "[1, 2, 3, 4, 5]"


def test_shift_by_6(s: Solution):
    nodes = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    nodes = s.rotateRight(nodes, 6)
    assert str(nodes) == "[5, 1, 2, 3, 4]"


def test_shift_by_7(s: Solution):
    nodes = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    nodes = s.rotateRight(nodes, 7)
    assert str(nodes) == "[4, 5, 1, 2, 3]"


def test_shift_by_negative_1(s: Solution):
    nodes = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    nodes = s.rotateRight(nodes, -1)
    assert str(nodes) == "[2, 3, 4, 5, 1]"


def test_shift_by_negative_2(s: Solution):
    nodes = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    nodes = s.rotateRight(nodes, -2)
    assert str(nodes) == "[3, 4, 5, 1, 2]"


def test_shift_by_negative_5(s: Solution):
    nodes = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    nodes = s.rotateRight(nodes, -5)
    assert str(nodes) == "[1, 2, 3, 4, 5]"


def test_shift_by_negative_6(s: Solution):
    nodes = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    nodes = s.rotateRight(nodes, -6)
    assert str(nodes) == "[2, 3, 4, 5, 1]"
