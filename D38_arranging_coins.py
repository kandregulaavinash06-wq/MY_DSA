# Day 38 - LeetCode #441: Arranging Coins
# https://leetcode.com/problems/arranging-coins/
#
# Given n coins, build a staircase where the ith row
# contains exactly i coins.
#
# Return the number of complete rows that can be built.
#
# I tried three different approaches:
# 1. Mathematical formula
# 2. Binary Search
# 3. Iterative approach


import math


class Solution:

    # Approach 1: Mathematical Formula
    #
    # The total number of coins required to build k rows is:
    #
    #     k * (k + 1) / 2
    #
    # We need to find the largest k such that:
    #
    #     k * (k + 1) / 2 <= n
    #
    # Using the quadratic formula:
    #
    #     k = (sqrt(8n + 1) - 1) / 2
    #
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def arrangeCoins_math(self, n: int) -> int:
        return int((math.sqrt(8 * n + 1) - 1) // 2)


    # Approach 2: Binary Search
    #
    # Instead of checking every possible row,
    # use binary search to find the maximum number
    # of complete rows.
    #
    # For a candidate m, calculate the number of coins
    # needed to build m complete rows.
    #
    # If the required coins are equal to n, we found
    # the exact answer.
    #
    # If fewer coins are required, try a larger value.
    #
    # If more coins are required, try a smaller value.
    #
    # Time Complexity: O(log n)
    # Space Complexity: O(1)

    def arrangeCoins_binary_search(self, n: int) -> int:
        l, r = 0, n
        res = 0

        while l <= r:
            m = (l + r) // 2
            needed = (m * (m + 1)) // 2

            if needed == n:
                return m

            elif needed < n:
                l = m + 1
                res = m

            else:
                r = m - 1

        return res


    # Approach 3: Iterative Approach
    #
    # Start with the first row and subtract the number
    # of coins required for each row.
    #
    # Continue until there aren't enough coins to build
    # the next complete row.
    #
    # Time Complexity: O(sqrt(n))
    # Space Complexity: O(1)

    def arrangeCoins_iterative(self, n: int) -> int:
        s = n

        if n <= 1:
            return 1

        for i in range(1, (s // 2) + 2):
            n -= i

            if n < 0:
                return i - 1

            if n == 0:
                return i