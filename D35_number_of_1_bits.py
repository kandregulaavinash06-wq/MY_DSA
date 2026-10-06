# Day 35 - LeetCode #191: Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/
#
# Given a positive integer n, return the number of set bits (1s)
# in its binary representation.
#
# I tried three different approaches.


class Solution:

    # Approach 1: Repeatedly divide by 2
    #
    # n % 2 gives the last binary digit.
    # If it is 1, increment the counter.
    # Then divide n by 2 to remove the last binary digit.
    #
    # Time Complexity: O(log n)
    # Space Complexity: O(1)

    def hammingWeight_division(self, n: int) -> int:
        c = 0

        while n:
            if n % 2 == 1:
                c += 1

            n //= 2

        return c


    # Approach 2: Convert the number to binary manually
    #
    # Extract each binary digit using n % 2 and build
    # the binary representation as a string.
    # Then count how many '1's are present.
    #
    # Time Complexity: O(log n)
    # Space Complexity: O(log n)

    def hammingWeight_string(self, n: int) -> int:
        res = ""

        while n:
            res = str(n % 2) + res
            n //= 2

        c = 0

        for i in res:
            if i == "1":
                c += 1

        return c


    # Approach 3: Using Python's built-in bin()
    #
    # bin(n) converts the number into its binary representation.
    # count("1") then counts the set bits directly.
    #
    # Time Complexity: O(log n)
    # Space Complexity: O(log n)

    def hammingWeight_bin(self, n: int) -> int:
        return bin(n).count("1")