class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        l1 = []
        maximum = max(candies)

        for i in candies:
            if i + extraCandies >= maximum:
                valid = True
            else:
                valid = False

            l1.append(valid)

        return l1