# Design and implement a TwoSum class. It should support the following operations: add and find.

# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.

# Example 1:

# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false

# Example 2:

# add(3); add(1); add(2);
# find(3) -> true
# find(6) -> false


class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.nums:   
            self.nums[number]+=1
        else:
            self.nums[number] = 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        res = False
        for n, count in self.nums.items():
            self.nums[n] -= 1
            if value-n in self.nums and self.nums[value-n]:
                res = True
            self.nums[n] += 1
        return res
        

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

