# This class is used to declare a Linked List
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# This function converts the passed list into a linked list and returns the head of the Linked List
def listToLink(lst : list) -> ListNode:
    dummy = curr = ListNode()
    for i in lst:
        curr.next = ListNode(i)
        curr = curr.next
    return dummy.next

# This function converts all the nodes from the linked list passed as a head in this function, into list
def linkToList(head: ListNode) -> list:
    l = []
    while head:
        l.append(head.val)
        head = head.next
    return l

# This funtion returns the length of the linked list
def length(head: ListNode) -> int:
    n = 0
    while head:
        head = head.next
        n += 1
    return n

# This function appends the value passed into the function into the linked list
def append(self, val: int) -> None:
    curr = ListNode(None, self)
    while curr.next:
        curr = curr.next
    curr.next = ListNode(val)

# This function appends the value from the left passed into the function into the linked list
def appendleft(self, val: int) -> ListNode:
    return ListNode(val, self)

# This function inserts the passed value at the provided index into the Linked List and returns the resulting head
def insert(self, val: int, index: int) -> ListNode:
    dummy = curr = ListNode(None, self)
    while index > 0:
        curr = curr.next
        index -= 1
    curr.next = ListNode(val, curr.next)
    return dummy.next

# This function deletes the tail node
def pop(self) -> None:
    if not self: return
    curr = ListNode(None, self)
    while curr.next.next:
        curr = curr.next
    curr.next = None
    self = curr.next

# This function deletes the head node and returns the resulting head node
def popleft(self) -> ListNode:
    if not self:
        return None
    newHead = self.next
    self.next = None
    return newHead

# This function deletes the node at the given index and returns the resulting head node
def delete(self, index: int) -> ListNode:
    if not self: return
    dummy = curr = ListNode(None, self)
    while index > 0:
        curr = curr.next
        index -= 1
    curr.next = curr.next.next
    return dummy.next

# This function remove the number of instances (count) of an integer in the Linked List and returns the resulting head node
def remove(self, val: int, count: int = 1) -> ListNode:
    # if count <= 0, then remove all
    dummy = curr = ListNode(None, self)
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
            count -= 1
            if count == 0: break
        else:
            curr = curr.next
    return dummy.next

# This function finds the first instance of an element in the Linked List and returns the index
def find(self, val: int) -> int:
    curr = self
    index = -1
    while curr:
        if index < 0: index = 0
        if curr.val == val:
            return index
        curr = curr.next
        index += 1
    return index

# This function counts and returns the number of instances of the given integer in the Linked List 
def count(self, val: int) -> int:
    curr = self
    n = 0
    while curr:
        if curr.val == val:
            n += 1
        curr = curr.next
    return n

# This function reverses the linked list and returns the new head node i.e. the tail node of the given Linked list
def reverse(self) -> ListNode:
    left = None
    curr = self
    while curr: 
        right = curr.next
        curr.next = left
        left = curr
        curr = right
    return left

# This function sorts the list using Merge Sort and returns the head of the sorted Linked list
def sortll(head: ListNode)-> ListNode:
    
    def partition(head: ListNode)-> list[ListNode]:
        half = fast = ListNode(None, head)
        while fast and fast.next:
            half = half.next
            fast = fast.next.next
        secondhead = half.next
        half.next = None
        return [head, secondhead]

    # If the length of the linked list is 1 or 0
    if head == None or head.next == None:
        return head
    first, second = partition(head)

    # Bringing the length of the first and second halves to 1
    if first.next:
        first = sortll(first)
    if second.next:
        second = sortll(second)

    # Sorting the single nodes back into a empty linked list
    test1, test2 = first, second
    dummy = curr = ListNode()
    while test1 or test2:
        if test1 and (not test2 or test1.val < test2.val):
            curr.next = test1
            test1 = test1.next
        else:
            curr.next = test2
            test2 = test2.next
        curr = curr.next
    return dummy.next
    
# This function prints out the linked list by using the passed head node
def printll(head: ListNode) -> None:
    curr = head
    while curr:
        print(curr.val, end = ' -> ')
        curr = curr.next
    print("None")