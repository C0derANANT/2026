# # Learning Vectors

v1 = [1, 2, 3]
v2 = [4, 5, 6]
# Addition
result = [a + b for a, b in zip(v1, v2)]
print(result)  # [5, 7, 9]
# Scalar multiplication
result = [2 * x for x in v1]
print(result)  # [2, 4, 6]
# Dot product
dot = sum(a * b for a, b in zip(v1, v2))
print(dot)  # 32


# LeetCode Problem

class Solution:
    def singleNumber(self, nums):
        s1 = set(nums)

        for i in s1:
            if nums.count(i) == 1:
                return i
