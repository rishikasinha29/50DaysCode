class Solution:
    def signFunc(self, x: int) -> int:
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0

    def arraySign(self, nums: list[int]) -> int:
        product = 1
        for num in nums:
            product *= num
        return self.signFunc(product)
