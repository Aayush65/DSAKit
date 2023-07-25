# This class is used to implement a Trie data structure for efficient word storage and retrieval
from os import system
system("cls")

class Trie:
    # Initialize the Trie data structure with an empty child dictionary and isWord flag
    def __init__(self):
        self.child = {}
        self.isWord = False

    # Add a word to the Trie data structure
    def addWord(self, word: str) -> None:
        curr = self
        for i in word:
            if i not in curr.child:
                # If the current character does not exist in the Trie, create a new node for it
                curr.child[i] = Trie()
            curr = curr.child[i]
        # Mark the last node as a complete word
        curr.isWord = True

    # Search for a word in the Trie data structure
    def search(self, word: str) -> bool:
        curr = self
        for i in word:
            if i not in curr.child:
                # If any character is not found, the word does not exist in the Trie
                return False
            curr = curr.child[i]
        # If the last node is marked as a complete word, the word exists in the Trie
        return curr.isWord

    # Check if any word in the Trie starts with the given prefix
    def startsWith(self, prefix: str) -> bool:
        curr = self
        for i in prefix:
            if i not in curr.child:
                # If any character is not found, no word starts with the given prefix
                return False
            curr = curr.child[i]
        # At least one word starts with the given prefix
        return True