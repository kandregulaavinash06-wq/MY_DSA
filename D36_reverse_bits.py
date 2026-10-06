# Day 36 - LeetCode #190: Reverse Bits
# https://leetcode.com/problems/reverse-bits/
#
# Reverse the bits of a given 32-bit integer.
#
# I tried two approaches:
# 1. Bit manipulation
# 2. String-based approach


class Solution:

    # Approach 1: Bit Manipulation
    #
    # Process exactly 32 bits.
    #
    # n & 1 extracts the last bit of n.
    # res << 1 shifts the result left to make space for
    # the next bit.
    # | b adds the extracted bit to the result.
    # n >> 1 removes the last bit from n.
    #
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def reverseBits_bit_manipulation(self, n: int) -> int:
        res = 0

        for i in range(32):
            b = n & 1
            res = (res << 1) | b
            n >>= 1

        return res


    # Approach 2: String-based approach
    #
    # Extract each bit using n % 2 and append it to a string.
    # Since the bits are extracted from right to left, appending
    # them in the same order automatically reverses the bits.
    #
    # int(res, 2) converts the reversed binary string back
    # into an integer.
    #
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    #
    # The loop always runs exactly 32 times, so both the
    # time and extra space are constant for this problem.

    def reverseBits_string(self, n: int) -> int:
        res = ""

        for i in range(32):
            res = res + str(n % 2)
            n //= 2

        return int(res, 2)