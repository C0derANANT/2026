class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        new = []
        total = 0

        for i in nums:
            total += i
            new.append(total)

        return new