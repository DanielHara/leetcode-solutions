# Question 2166: https://leetcode.com/problems/design-bitset/

"""
    Very interesting question! Just use sets to save the positions where there are ones, and where there are zeros.
    When you flip, you just need to swap both sets, making operations "fix", "unfix", "flip", "all", "one" and "count"
    run in O(1) time.
"""

class Bitset:
    def __init__(self, size: int):
        self.count_1_bits = 0
        self.size = size
        self.one_bit_positions = set()
        self.zero_bit_positions = set()
        for index in range(size):
            self.zero_bit_positions.add(index)

    def fix(self, idx: int) -> None:
        self.one_bit_positions.add(idx)
        if idx in self.zero_bit_positions:
            self.zero_bit_positions.remove(idx)

    def unfix(self, idx: int) -> None:
        self.zero_bit_positions.add(idx)
        if idx in self.one_bit_positions:
            self.one_bit_positions.remove(idx)

    def flip(self) -> None:
        one_bit_positions = self.one_bit_positions
        self.one_bit_positions = self.zero_bit_positions
        self.zero_bit_positions = one_bit_positions

    def all(self) -> bool:
        return len(self.one_bit_positions) == self.size

    def one(self) -> bool:
        return len(self.one_bit_positions) > 0

    def count(self) -> int:
        return len(self.one_bit_positions)

    def toString(self) -> str:
        array = []
        for index in range(self.size):
            if index in self.one_bit_positions:
                array.append('1')
            else:
                array.append('0')
        return ''.join(array)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()