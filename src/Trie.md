# Trie Module

Trie Module is a Python module that provides an implementation of the Trie data structure for efficient word storage and retrieval.

## Class

### `Trie`

The `Trie` class represents a Trie data structure. It provides the following methods:

1. `__init__(self)`
   - Initializes an empty Trie data structure.
   - Time Complexity: O(1)
   - Space Complexity: O(1)

2. `addWord(self, word: str) -> None`
   - Adds a word to the Trie data structure.
   - Time Complexity: O(m), where m is the length of the word
   - Space Complexity: O(m), where m is the length of the word

3. `search(self, word: str) -> bool`
   - Searches for a word in the Trie data structure and returns True if found, False otherwise.
   - Time Complexity: O(m), where m is the length of the word
   - Space Complexity: O(1)

4. `startsWith(self, prefix: str) -> bool`
   - Checks if any word in the Trie starts with the given prefix and returns True if found, False otherwise.
   - Time Complexity: O(m), where m is the length of the prefix
   - Space Complexity: O(1)

## Usage

1. Import the `dsakit` from pip using:

```python
pip install dsakit
```

2. Import class/functions from Trie as needed:

```python
from Trie import *
```

## Example

1. Create a Trie and add words to it:

```python
trie = Trie()
trie.addWord("apple")
trie.addWord("banana")
trie.addWord("orange")
```

2. Search for words in the Trie:

```python
print(trie.search("apple"))   # Output: True
print(trie.search("grape"))   # Output: False
```

3. Check if any word starts with a given prefix:

```python
print(trie.startsWith("app"))    # Output: True
print(trie.startsWith("ban"))    # Output: True
print(trie.startsWith("ora"))    # Output: True
print(trie.startsWith("gr"))     # Output: False
```