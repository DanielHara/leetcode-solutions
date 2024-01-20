"""
    Question 2424: https://leetcode.com/problems/longest-uploaded-prefix/

    An easy solution passes the judge.
"""

class LUPrefix:
    def __init__(self, n: int):
        self.set = set()
        self.longest_prefix = 0

    def upload(self, video: int) -> None:
        self.set.add(video)

        while (self.longest_prefix + 1) in self.set:
            self.longest_prefix = self.longest_prefix + 1

    def longest(self) -> int:
        return self.longest_prefix



# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()