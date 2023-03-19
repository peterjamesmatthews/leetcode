"""
Design a data structure that supports adding new words and finding if a string matches any
previously added string.
"""


class Node:
    def __init__(self):
        self.ending = False  # `True` if a word ends with this node, otherwise `False`
        self.children: dict[str, Node] = {}  # Maps subsequent characters to their nodes


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds word to this `WordDictionary`

        #### Arguments
            `word: str` Word that will be added to the `WordDictionary`

        #### Example
        ```py
        wd = WordDictionary()   # {}
        wd.addWord("foo")       # { "foo" }
        wd.addWord("bar")       # { "foo", "bar" }
        ```
        """
        current = self.root
        for character in word:
            if character not in current.children.keys():
                current.children[character] = Node()
            current = current.children[character]
        current.ending = True

    def search(self, word: str) -> bool:
        """
        Returns `True` if there is any string in this `WordDictionary` that matches word or
        `False` otherwise. `word` may contain dots `.` where dots can be matched with any letter.

        #### Arguments
            `word: str` Word to search for in this `WordDictionary`. `.` will match any letter.

        #### Returns
            `bool` `True` if `word` is in this `WordDictionary`, otherwise `False`

        #### Example
        ```py
        wd = WordDictionary()   # {}
        wd.addWord("foo")       # { "foo" }
        wd.search("bar")        # returns False
        wd.search("foo")        # returns True
        wd.search(".oo")        # return True
        ```
        """
        return self._search(self.root, word, 0)

    def _search(self, current: Node, word: str, i: int) -> bool:
        if i == len(word):
            return current.ending

        paths: list[Node] = []  # all nodes that may contain the rest of this word
        if word[i] == ".":
            paths.extend(current.children.values())
        elif word[i] in current.children:
            paths.append(current.children[word[i]])

        # search each path for a match
        for path in paths:
            if self._search(path, word, i + 1):
                return True
        return False
