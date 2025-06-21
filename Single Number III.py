class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for i in nums:
            xor_all ^= i
        rightmost_bit = xor_all & -xor_all
        x=y=0
        for num in nums:
            if num & rightmost_bit:
                x^=num
            else:
                y^=num
        return [x,y]
