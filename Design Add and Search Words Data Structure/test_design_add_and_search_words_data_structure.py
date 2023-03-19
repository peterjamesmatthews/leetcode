from design_add_and_search_words_data_structure import WordDictionary
from pytest import fixture


@fixture
def wd() -> WordDictionary:
    return WordDictionary()


def test_example(wd: WordDictionary):
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")

    assert wd.search("pad") == False
    assert wd.search("bad") == True
    assert wd.search(".ad") == True
    assert wd.search("..d") == True


def test_empty(wd: WordDictionary):
    assert wd.search("foo") == False
    assert wd.search(".") == False
    assert wd.search("...") == False


def test_f(wd: WordDictionary):
    wd.addWord("foo")
    wd.addWord("f")
    assert wd.search("f")
    assert wd.search("foo")
    assert not wd.search("b")


def test_foo(wd: WordDictionary):
    wd.addWord("at")
    wd.addWord("and")
    wd.addWord("an")
    wd.addWord("add")
    assert not wd.search("a")
    assert not wd.search(".at")
    wd.addWord("bat")
    assert wd.search(".at")
    assert wd.search("an.")
    assert not wd.search("a.d.")
    assert not wd.search("b.")
    assert wd.search("a.d")
    assert not wd.search(".")
