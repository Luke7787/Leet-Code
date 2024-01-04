class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        reverse_bit = 0
        for _ in range(32):
            reverse_bit = reverse_bit << 1 | n & 1
            n >>= 1
        return reverse_bit