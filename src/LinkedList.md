# LinkedListModule

LinkedListModule is a Python module that provides efficient functions for working with Linked Lists.

## Initialise

Initialise a node of linked list:
```python
head = ListNode(0) # Creates a node with value 0 and next node NULL
```


## Functions

1. `listToLink(lst)`
   - Converts a given list into a linked list and returns the head of the linked list.
   - Time Complexity: O(n)
   - Space Complexity: O(1)

2. `linkToList(head)`
   - Converts a linked list into a list.
   - Time Complexity: O(n)
   - Space Complexity: O(n)
   
3. `length(head)`
   - Returns the length of the linked list.
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   
4. `append(head, val)`
   - Appends a value to the end of the linked list and returns the resulting head.
   - This function can be used directly without assigning the returned head to another variable, except for an empty linked list.
   - Time Complexity: O(n)
   - Space Complexity: O(1)

5. `insert(head, val, index)`
   - Inserts a value at the specified index in the linked list and returns the resulting head.
   - This function can be used directly without assigning the returned head to another variable, except when inserting at the 0th index or dealing with an empty linked list.
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   
6. `pop(head)`
   - Deletes the tail node and returns the resulting head node.
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   
7. `delete(head, index)`
   - Deletes the node at the specified index in the linked list and returns the resulting head node.
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   
8. `remove(head, val, count=1)`
   - Removes the specified number of instances (count) of an integer from the linked list and returns the resulting head node.
   - The default value of count is set to 1, which deletes only one occurrence of the given integer from the linked list.
   
9. `find(head, val)`
   - Finds the first instance of an element in the linked list and returns its index.
   - If the element is not found, it returns -1.
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   
10. `count(head, val)`
    - Counts and returns the number of instances of a given integer in the linked list.
    - Time Complexity: O(n)
    - Space Complexity: O(1)

11. `reverse(head)`
    - Reverses the linked list and returns the new head node (i.e., the previous tail node).
    - Time Complexity: O(n)
    - Space Complexity: O(1)

12. `sortll(head)`
    - Sorts the linked list using Merge Sort and returns the head of the sorted Linked list.
    - Time Complexity: O(n log n)
    - Space Complexity: O(log n)

13. `printll(head)`
    - Prints the linked list using the given head node.
    - Time Complexity: O(n)
    - Space Complexity: O(1)

## Example

1. Create a linked list from a list and print the linked list along with its length:

```python
lst = [1, 2, 3, 4, 5]
head = listToLink(lst)
length = length(head)
printll(head)
print(length)
```

2. Convert a linked list to a list:

```python
lst = linkToList(head)
print(lst)
```

3. Append a value to the beginning and end of the linked list:

```python
head.appendleft(0)
head.append(6)
printll(head)
```

4. Insert a value in the linked list

```python
head.insert(0)
head.append(6)
printll(head)
```

5. Delete or remove index and values respectively from linked list

```python
head.remove(2)
head.delete(1)
printll(head)
```

6. Find the index or count occurances of a value:

```python
printll(head.find(4))
printll(head.count(6))
```

7. Sort the linked list:

```python
head = listToLink([2,4,3,2,8])
head = sortll(head)
printll(head) # 2 -> 2 -> 3 -> 4 -> 8
```