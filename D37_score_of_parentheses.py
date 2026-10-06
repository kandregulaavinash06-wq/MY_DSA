# Day 37 - LeetCode #856: Score of Parentheses
# https://leetcode.com/problems/score-of-parentheses/
#
# Given a balanced parentheses string, calculate its score.
#
# Rules:
# "()" has score 1
# AB has score A + B
# (A) has score 2 * A
#
# Approach:
# Use the current depth of the parentheses.
# Whenever we find a complete "()" pair, its score is
# 2 raised to the current depth.


class Solution:

    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0

        for i in range(len(s)):

            if s[i] == '(':
                # Entering a deeper level of nesting.
                depth += 1

            else:
                # Closing the current pair.
                depth -= 1

                # If the previous character was '(',
                # we have found a primitive "()" pair.
                if s[i - 1] == '(':
                    # A pair at this depth contributes 2^depth.
                    score += (1 << depth)

        return score


# Time Complexity: O(n)
# Space Complexity: O(1)