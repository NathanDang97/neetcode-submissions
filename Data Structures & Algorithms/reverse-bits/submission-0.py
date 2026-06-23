class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_bits = 0
        for i in range(32):
            # extract the ith bit of n
            bit = (n >> i) & 1
            # shift this bit to position (31 - i)
            # and add it to the result
            reversed_bits += (bit << (31 - i))
        return reversed_bits