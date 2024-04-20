from typing import Callable, List, Optional

class SegmentTree:

    def __init__(self, nums: List[int], identity_val: Optional[int], cmp: Callable, key: Callable = lambda x: x):
        self.__n = len(nums)
        self.__identity_val = identity_val
        self.__key = key
        self.__cmp = cmp

        self.__nums = nums
        self.__build_nums()
        self.__tree = [identity_val] * self.__n * 2
        self.__build_tree()

    # Prints the segment tree when the Object is printed
    def __str__(self) -> str:
        return self.__tree.__str__()
    
    # This function builds the main array at initial initialisation using key function
    def __build_nums(self):
        self.__nums = [self.__key(x) for x in self.__nums]

    # This function builds the segment tree at initial initialisation
    def __build_tree(self):
        for i in range(self.__n):
            self.__tree[i + self.__n] = self.__nums[i]
        for i in range(self.__n - 1, 0, -1):
            self.__tree[i] = self.__cmp(self.__tree[2 * i], self.__tree[2 * i + 1])

    # This function updates the values at the index to the new value
    def update(self, index: int, val: int):
        index += self.__n
        self.__tree[index] = val
        while index > 1:
            new_val = self.__cmp(self.__tree[index], self.__tree[index ^ 1])
            index //= 2
            if self.__tree[index] == new_val:
                break
            self.__tree[index] = new_val

    # This function removes all the instances of the val from the tree
    def remove(self, val: int) -> int:
        removed = 0
        for i in range(self.__n):
            if self.__tree[self.__n + i] == val:
                self.update(i, self.__identity_val)
                removed += 1
        return removed
    
    # This function removes the instance of the element at the passed index
    def pop(self, index: int) -> int:
        poped = self.__nums[index + self.__n]
        self.update(index, self.__identity_val)
        return poped

    # This function returns the result between the left and right indices (not inclusive)
    def query(self, left: int, right: int) -> int:
        res = self.__identity_val
        left += self.__n
        right += self.__n + 1
        while left < right:
            if left & 1:
                res = self.__cmp(res, self.__tree[left])
                left += 1
            if right & 1:
                right -= 1
                res = self.__cmp(res, self.__tree[right])
            left //= 2
            right //= 2
        return res